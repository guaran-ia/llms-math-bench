import contextlib, io, json, unittest, tempfile
from urllib.error import HTTPError
from unittest.mock import patch
from pathlib import Path
from src.dataset import DATASETS, LANGUAGES, load_dataset, problem_text
from src.prompting import CONDITIONS, PROMPT_SET, render_prompt
from src.model_config import MODEL_CONFIGS, resolve_models
from src.run_benchmark import planned_call_count, parse_args, run, _dump_usage, _model_version
from src.report_benchmark import make_report, mcnemar, holm, main as report_main
from src.math_evaluation import evaluate
from src.model_metadata import discover_model_metadata
import src.math_evaluation as evaluator

class FakeUsage:
    def model_dump(self, exclude_none=True): return {"total_tokens": 17}
class FakeResponse: model="returned-model-x"; usage=FakeUsage()

class NewStudyTests(unittest.TestCase):
    def test_complete_crossed_prompt_rendering_and_reasoning_labels(self):
        self.assertEqual(len(CONDITIONS),7)
        self.assertTrue(all("source_prompts" not in condition for condition in CONDITIONS.values()))
        self.assertEqual(len(DATASETS),3)
        self.assertEqual(set(DATASETS),{"elementary","jr_highschool","k3_elementary"})
        for dataset in DATASETS:
            rows,_=load_dataset(dataset)
            for row in rows:
                for lang in LANGUAGES:
                    statement=problem_text(row,lang)
                    for condition in CONDITIONS:
                        prompt=render_prompt(condition,lang,statement,row)
                        self.assertIn(PROMPT_SET["role_instruction"][lang],prompt)
                        self.assertIn('"reasoning":"..."',prompt)
                        self.assertIn('"steps":["..."]',prompt)
                        self.assertIn('"final_answer":{"value":0}',prompt)
                        instruction=prompt.split("Problema:\n",1)[0].lower()
                        self.assertNotRegex(instruction,r'\b(?:grade|grado|año|years old|años)\b')
                        if condition=="reasoning_type": self.assertTrue(row.get("reasoning_type_id"))
    def test_all_reasoning_labels_resolve(self):
        labels=PROMPT_SET["reasoning_type_labels"]
        for dataset in DATASETS:
            rows,_=load_dataset(dataset)
            for row in rows: self.assertIn(row["reasoning_type_id"],labels)
    def test_model_routing_only_five_selected(self):
        models=resolve_models()
        self.assertEqual(len(models),5)
        self.assertEqual({m["model_id"] for m in models},set(MODEL_CONFIGS))
        self.assertEqual(MODEL_CONFIGS["gemini-3.5-flash"].provider,"gemini-api")
        self.assertEqual(sum(c.provider.startswith("azure") for c in MODEL_CONFIGS.values()),4)
        resolved=resolve_models(environ={"AZURE_AI_SERVICES_ENDPOINT":"","AZURE_OPENAI_ENDPOINT":""})
        self.assertTrue(all(m["endpoint"] for m in resolved))
        self.assertEqual(next(m for m in resolved if m["model_id"]=="gpt-4o-mini")["api_version"],"2024-12-01-preview")
    def test_full_matrix_is_2800_and_dry_run_has_no_calls(self):
        self.assertEqual(planned_call_count(list(DATASETS),list(MODEL_CONFIGS),LANGUAGES,list(CONDITIONS)),2800)
        output=io.StringIO()
        with contextlib.redirect_stdout(output): run(parse_args(["--dry-run"]))
        summary=json.loads(output.getvalue())
        self.assertEqual(summary["planned_model_requests"],2800)
        self.assertEqual(summary["paid_api_calls"],0)
        self.assertEqual(Path(summary["output"]).parent.name,"results")
        self.assertNotEqual(Path(summary["output"]).parent.name,"new_study")
    def test_numeric_structured_and_symbolic_evaluation(self):
        self.assertTrue(evaluate({"expected_answer":1.5,"response":{"final_answer":{"value":"1.50001"}}})["correct"])
        self.assertTrue(evaluate({"expected_answer":[[1,2],[3,4]],"response":{"final_answer":{"value":[[1,2],[3,4]]}}})["correct"])
        if evaluator.sp is None: self.skipTest("SymPy is installed from requirements.txt; it is not installed in this environment.")
        self.assertTrue(evaluate({"expected_answer":"x^2+2*x+1","response":{"final_answer":{"value":"(x+1)^2"}}})["correct"])
        self.assertFalse(evaluate({"expected_answer":9,"response":{"reasoning":"There are 9","final_answer":{"value":8}}})["correct"])
    def test_gemini_metadata_discovery_updates_version_and_utc(self):
        class FakeHttpResponse:
            def __enter__(self): return self
            def __exit__(self,*args): return False
            def read(self): return b'{"name":"models/gemini-3.5-flash","version":"001"}'
        config={"provider":"gemini-api","model_id":"gemini-3.5-flash","deployment_id":"gemini-3.5-flash"}
        with patch("src.model_metadata.urlopen",return_value=FakeHttpResponse()):
            result=discover_model_metadata(config,"fixture-key")
        self.assertEqual(result["model_version"],"001")
        self.assertEqual(result["model_metadata_source"],"gemini_models_get")
        self.assertTrue(result["model_metadata_checked_at_utc"].endswith("Z"))
    def test_metadata_only_cli_does_not_initialize_inference(self):
        output=io.StringIO()
        fake={"model_version":"001","provider_model_id":"models/gemini-3.5-flash","model_metadata_checked_at_utc":"2026-11-12T00:00:00Z","model_metadata_source":"gemini_models_get","model_metadata_status":"version_found"}
        with patch.dict("os.environ",{"GEMINI_API_KEY":"fixture-key"}), \
             patch("src.run_benchmark.discover_model_metadata",return_value=fake), \
             patch("src.run_benchmark.create_client",side_effect=AssertionError("client must not be created")), \
             contextlib.redirect_stdout(output):
            run(parse_args(["--models","gemini-3.5-flash","--check-model-metadata"]))
        result=json.loads(output.getvalue())
        self.assertEqual(result["paid_api_calls"],0)
        self.assertEqual(result["models"][0]["model_version"],"001")
    def test_gemini_metadata_error_reports_provider_diagnostic(self):
        body=io.BytesIO(b'{"error":{"message":"Model is not available to this API key."}}')
        failure=HTTPError("https://example.invalid",400,"Bad Request",{},body)
        with patch("src.model_metadata.urlopen",side_effect=failure):
            with self.assertRaisesRegex(RuntimeError,"Model is not available to this API key"):
                discover_model_metadata({"provider":"gemini-api","deployment_id":"gemini-3.5-flash"},"not-printed")
    def test_azure_metadata_discovery_uses_deployment_details(self):
        config={"provider":"azure-ai-services","endpoint":"https://example.services.ai.azure.com/openai/v1","deployment_id":"Llama-3.3-70B-Instruct"}
        account=[{"name":"example","resourceGroup":"rg-study"}]
        deployment={"name":"Llama-3.3-70B-Instruct","properties":{"model":{"name":"Llama-3.3-70B-Instruct","version":"3.3","format":"Meta"}}}
        with patch("src.model_metadata._az_json",side_effect=[account,deployment]) as mocked:
            result=discover_model_metadata(config,"fixture-key",{"AZURE_SUBSCRIPTION_ID":"sub-fixture"})
        self.assertEqual(result["model_version"],"3.3")
        self.assertEqual(result["model_metadata_source"],"azure_resource_manager_deployment")
        self.assertEqual(mocked.call_count,2)
        self.assertTrue(result["model_metadata_checked_at_utc"].endswith("Z"))
    def test_response_metadata_capture_helpers(self):
        self.assertEqual(_dump_usage(FakeResponse()),{"total_tokens":17})
        self.assertEqual(_model_version(None,{},FakeResponse()),"returned-model-x")
    def test_paired_stats_and_report(self):
        self.assertEqual(mcnemar([True,False],[False,False]),(1,0,1.0))
        self.assertEqual(holm([("a",.01),("b",.02)]),[(.01,.02),(.02,.02)])
        rows=[]
        for lang,correct in (("es",True),("gn",False)):
            rows.append({"dataset_id":"elementary","problem_id":1,"model_id":"m","language":lang,
              "prompt_condition_id":"standard","expected_answer":2 if correct else 3,
              "response":{"final_answer":{"value":2}}})
        report=make_report(rows,"fixture.jsonl")
        self.assertIn("Paired Spanish–Guaraní comparisons",report)
        self.assertIn("Prompt comparisons against standard",report)
        self.assertIn("1/1",report)
        with tempfile.TemporaryDirectory() as tmp:
            inp=Path(tmp)/"fixture.jsonl"; out=Path(tmp)/"report.md"
            inp.write_text("\n".join(json.dumps({k:v for k,v in row.items() if k!="_score"}) for row in rows),encoding="utf-8")
            report_main(["--input",str(inp),"--output",str(out)])
            self.assertTrue(out.exists())
            self.assertIn("Prompt comparisons against standard",out.read_text(encoding="utf-8"))

if __name__=="__main__": unittest.main()
