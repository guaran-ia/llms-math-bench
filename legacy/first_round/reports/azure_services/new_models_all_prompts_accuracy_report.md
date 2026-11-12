# Prompt Accuracy Report by Model

## Summary

- Evaluated file: `model_test_results_new_models_all_prompts.jsonl`
- Attempts read: 180
- Attempts evaluated for ranking: 180
- Invalid JSONL lines: 0
- Best combination: **azure-services-responses / gpt-5.5 / v7** (10/10)

## Ranking by Prompt

| Rank | Provider | Model | Prompt | Name | Correct answers | Accuracy | Valid JSON | Consistent option | API errors | JSON errors | Mean latency |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | azure-services-responses | gpt-5.5 | v7 | Bilingual teacher with glossary and warmup | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 7.150s |
| 2 | azure-services-responses | gpt-5.5 | v4 | Bilingual teacher with glossary | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 7.258s |
| 3 | azure-services-responses | gpt-5.5 | v3 | Bilingual teacher with semantic interpretation | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 7.465s |
| 4 | azure-services-responses | gpt-5.5 | v2 | Internal translation into Spanish | 10/10 | 100.0% | 10/10 | 10/10 | 0 | 0 | 7.814s |
| 5 | azure-services-responses | gpt-5.5 | v8 | Simple zero-shot autocomplete | 10/10 | 100.0% | 0/10 | 0/10 | 0 | 0 | 3.934s |
| 6 | azure-services-responses | gpt-5.5 | v9 | Simple few-shot autocomplete | 10/10 | 100.0% | 0/10 | 0/10 | 0 | 0 | 4.091s |
| 7 | azure-services-responses | gpt-5.5 | v1 | Strict Guaraní | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 10.127s |
| 8 | azure-services-responses | gpt-5.5 | v5 | Strict Guaraní with reinforced JSON rules | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 10.438s |
| 9 | azure-services-responses | gpt-5.5 | v6 | Strict Guaraní with reinforced JSON rules and warmup | 9/10 | 90.0% | 10/10 | 10/10 | 0 | 0 | 11.085s |
| 10 | azure-services-responses | gpt-5.6-terra | v9 | Simple few-shot autocomplete | 9/10 | 90.0% | 0/10 | 0/10 | 0 | 0 | 3.285s |
| 11 | azure-services-responses | gpt-5.6-terra | v7 | Bilingual teacher with glossary and warmup | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 4.013s |
| 12 | azure-services-responses | gpt-5.6-terra | v2 | Internal translation into Spanish | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 4.175s |
| 13 | azure-services-responses | gpt-5.6-terra | v4 | Bilingual teacher with glossary | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 4.349s |
| 14 | azure-services-responses | gpt-5.6-terra | v3 | Bilingual teacher with semantic interpretation | 8/10 | 80.0% | 10/10 | 10/10 | 0 | 0 | 4.727s |
| 15 | azure-services-responses | gpt-5.6-terra | v5 | Strict Guaraní with reinforced JSON rules | 7/10 | 70.0% | 10/10 | 10/10 | 0 | 0 | 5.107s |
| 16 | azure-services-responses | gpt-5.6-terra | v6 | Strict Guaraní with reinforced JSON rules and warmup | 7/10 | 70.0% | 10/10 | 10/10 | 0 | 0 | 5.516s |
| 17 | azure-services-responses | gpt-5.6-terra | v1 | Strict Guaraní | 7/10 | 70.0% | 10/10 | 10/10 | 0 | 0 | 5.955s |
| 18 | azure-services-responses | gpt-5.6-terra | v8 | Simple zero-shot autocomplete | 7/10 | 70.0% | 0/10 | 0/10 | 0 | 0 | 3.152s |

## Per-Problem Details

| Prompt | Problem | Model | Expected | Predicted | Correct | Valid JSON | Line |
|---|---:|---|---:|---:|---|---|---:|
| v1 | 1 | gpt-5.5 | 18 | 10 | no | yes | 2 |
| v1 | 1 | gpt-5.6-terra | 18 | 10 | no | yes | 1 |
| v1 | 2 | gpt-5.5 | 8 | 8 | yes | yes | 4 |
| v1 | 2 | gpt-5.6-terra | 8 | 8 | yes | yes | 3 |
| v1 | 3 | gpt-5.5 | 140 | 140 | yes | yes | 6 |
| v1 | 3 | gpt-5.6-terra | 140 | 140 | yes | yes | 5 |
| v1 | 4 | gpt-5.5 | 600 | 600 | yes | yes | 8 |
| v1 | 4 | gpt-5.6-terra | 600 | 600 | yes | yes | 7 |
| v1 | 5 | gpt-5.5 | 3 | 3 | yes | yes | 10 |
| v1 | 5 | gpt-5.6-terra | 3 | 3 | yes | yes | 9 |
| v1 | 6 | gpt-5.5 | 60 | 60 | yes | yes | 12 |
| v1 | 6 | gpt-5.6-terra | 60 | 30 | no | yes | 11 |
| v1 | 7 | gpt-5.5 | 91 | 91 | yes | yes | 14 |
| v1 | 7 | gpt-5.6-terra | 91 | 91 | yes | yes | 13 |
| v1 | 8 | gpt-5.5 | 360 | 360 | yes | yes | 16 |
| v1 | 8 | gpt-5.6-terra | 360 | 120 | no | yes | 15 |
| v1 | 9 | gpt-5.5 | 8 | 8 | yes | yes | 18 |
| v1 | 9 | gpt-5.6-terra | 8 | 8 | yes | yes | 17 |
| v1 | 10 | gpt-5.5 | 34 | 34 | yes | yes | 20 |
| v1 | 10 | gpt-5.6-terra | 34 | 34 | yes | yes | 19 |
| v2 | 1 | gpt-5.5 | 18 | 18 | yes | yes | 22 |
| v2 | 1 | gpt-5.6-terra | 18 | 10 | no | yes | 21 |
| v2 | 2 | gpt-5.5 | 8 | 8 | yes | yes | 24 |
| v2 | 2 | gpt-5.6-terra | 8 | 8 | yes | yes | 23 |
| v2 | 3 | gpt-5.5 | 140 | 140 | yes | yes | 26 |
| v2 | 3 | gpt-5.6-terra | 140 | 140 | yes | yes | 25 |
| v2 | 4 | gpt-5.5 | 600 | 600 | yes | yes | 28 |
| v2 | 4 | gpt-5.6-terra | 600 | 600 | yes | yes | 27 |
| v2 | 5 | gpt-5.5 | 3 | 3 | yes | yes | 30 |
| v2 | 5 | gpt-5.6-terra | 3 | 3 | yes | yes | 29 |
| v2 | 6 | gpt-5.5 | 60 | 60 | yes | yes | 32 |
| v2 | 6 | gpt-5.6-terra | 60 | 60 | yes | yes | 31 |
| v2 | 7 | gpt-5.5 | 91 | 91 | yes | yes | 34 |
| v2 | 7 | gpt-5.6-terra | 91 | 91 | yes | yes | 33 |
| v2 | 8 | gpt-5.5 | 360 | 360 | yes | yes | 36 |
| v2 | 8 | gpt-5.6-terra | 360 | 120 | no | yes | 35 |
| v2 | 9 | gpt-5.5 | 8 | 8 | yes | yes | 38 |
| v2 | 9 | gpt-5.6-terra | 8 | 8 | yes | yes | 37 |
| v2 | 10 | gpt-5.5 | 34 | 34 | yes | yes | 40 |
| v2 | 10 | gpt-5.6-terra | 34 | 34 | yes | yes | 39 |
| v3 | 1 | gpt-5.5 | 18 | 18 | yes | yes | 42 |
| v3 | 1 | gpt-5.6-terra | 18 | 10 | no | yes | 41 |
| v3 | 2 | gpt-5.5 | 8 | 8 | yes | yes | 44 |
| v3 | 2 | gpt-5.6-terra | 8 | 8 | yes | yes | 43 |
| v3 | 3 | gpt-5.5 | 140 | 140 | yes | yes | 46 |
| v3 | 3 | gpt-5.6-terra | 140 | 140 | yes | yes | 45 |
| v3 | 4 | gpt-5.5 | 600 | 600 | yes | yes | 48 |
| v3 | 4 | gpt-5.6-terra | 600 | 600 | yes | yes | 47 |
| v3 | 5 | gpt-5.5 | 3 | 3 | yes | yes | 50 |
| v3 | 5 | gpt-5.6-terra | 3 | 3 | yes | yes | 49 |
| v3 | 6 | gpt-5.5 | 60 | 60 | yes | yes | 52 |
| v3 | 6 | gpt-5.6-terra | 60 | 60 | yes | yes | 51 |
| v3 | 7 | gpt-5.5 | 91 | 91 | yes | yes | 54 |
| v3 | 7 | gpt-5.6-terra | 91 | 91 | yes | yes | 53 |
| v3 | 8 | gpt-5.5 | 360 | 360 | yes | yes | 56 |
| v3 | 8 | gpt-5.6-terra | 360 | 120 | no | yes | 55 |
| v3 | 9 | gpt-5.5 | 8 | 8 | yes | yes | 58 |
| v3 | 9 | gpt-5.6-terra | 8 | 8 | yes | yes | 57 |
| v3 | 10 | gpt-5.5 | 34 | 34 | yes | yes | 60 |
| v3 | 10 | gpt-5.6-terra | 34 | 34 | yes | yes | 59 |
| v4 | 1 | gpt-5.5 | 18 | 18 | yes | yes | 62 |
| v4 | 1 | gpt-5.6-terra | 18 | 10 | no | yes | 61 |
| v4 | 2 | gpt-5.5 | 8 | 8 | yes | yes | 64 |
| v4 | 2 | gpt-5.6-terra | 8 | 8 | yes | yes | 63 |
| v4 | 3 | gpt-5.5 | 140 | 140 | yes | yes | 66 |
| v4 | 3 | gpt-5.6-terra | 140 | 140 | yes | yes | 65 |
| v4 | 4 | gpt-5.5 | 600 | 600 | yes | yes | 68 |
| v4 | 4 | gpt-5.6-terra | 600 | 600 | yes | yes | 67 |
| v4 | 5 | gpt-5.5 | 3 | 3 | yes | yes | 70 |
| v4 | 5 | gpt-5.6-terra | 3 | 3 | yes | yes | 69 |
| v4 | 6 | gpt-5.5 | 60 | 60 | yes | yes | 72 |
| v4 | 6 | gpt-5.6-terra | 60 | 60 | yes | yes | 71 |
| v4 | 7 | gpt-5.5 | 91 | 91 | yes | yes | 74 |
| v4 | 7 | gpt-5.6-terra | 91 | 91 | yes | yes | 73 |
| v4 | 8 | gpt-5.5 | 360 | 360 | yes | yes | 76 |
| v4 | 8 | gpt-5.6-terra | 360 | 120 | no | yes | 75 |
| v4 | 9 | gpt-5.5 | 8 | 8 | yes | yes | 78 |
| v4 | 9 | gpt-5.6-terra | 8 | 8 | yes | yes | 77 |
| v4 | 10 | gpt-5.5 | 34 | 34 | yes | yes | 80 |
| v4 | 10 | gpt-5.6-terra | 34 | 34 | yes | yes | 79 |
| v5 | 1 | gpt-5.5 | 18 | 10 | no | yes | 82 |
| v5 | 1 | gpt-5.6-terra | 18 | 10 | no | yes | 81 |
| v5 | 2 | gpt-5.5 | 8 | 8 | yes | yes | 84 |
| v5 | 2 | gpt-5.6-terra | 8 | 8 | yes | yes | 83 |
| v5 | 3 | gpt-5.5 | 140 | 140 | yes | yes | 86 |
| v5 | 3 | gpt-5.6-terra | 140 | 140 | yes | yes | 85 |
| v5 | 4 | gpt-5.5 | 600 | 600 | yes | yes | 88 |
| v5 | 4 | gpt-5.6-terra | 600 | 600 | yes | yes | 87 |
| v5 | 5 | gpt-5.5 | 3 | 3 | yes | yes | 90 |
| v5 | 5 | gpt-5.6-terra | 3 | 3 | yes | yes | 89 |
| v5 | 6 | gpt-5.5 | 60 | 60 | yes | yes | 92 |
| v5 | 6 | gpt-5.6-terra | 60 | 40 | no | yes | 91 |
| v5 | 7 | gpt-5.5 | 91 | 91 | yes | yes | 94 |
| v5 | 7 | gpt-5.6-terra | 91 | 91 | yes | yes | 93 |
| v5 | 8 | gpt-5.5 | 360 | 360 | yes | yes | 96 |
| v5 | 8 | gpt-5.6-terra | 360 | 120 | no | yes | 95 |
| v5 | 9 | gpt-5.5 | 8 | 8 | yes | yes | 98 |
| v5 | 9 | gpt-5.6-terra | 8 | 8 | yes | yes | 97 |
| v5 | 10 | gpt-5.5 | 34 | 34 | yes | yes | 100 |
| v5 | 10 | gpt-5.6-terra | 34 | 34 | yes | yes | 99 |
| v6 | 1 | gpt-5.5 | 18 | 10 | no | yes | 102 |
| v6 | 1 | gpt-5.6-terra | 18 | 10 | no | yes | 101 |
| v6 | 2 | gpt-5.5 | 8 | 8 | yes | yes | 104 |
| v6 | 2 | gpt-5.6-terra | 8 | 8 | yes | yes | 103 |
| v6 | 3 | gpt-5.5 | 140 | 140 | yes | yes | 106 |
| v6 | 3 | gpt-5.6-terra | 140 | 140 | yes | yes | 105 |
| v6 | 4 | gpt-5.5 | 600 | 600 | yes | yes | 108 |
| v6 | 4 | gpt-5.6-terra | 600 | 600 | yes | yes | 107 |
| v6 | 5 | gpt-5.5 | 3 | 3 | yes | yes | 110 |
| v6 | 5 | gpt-5.6-terra | 3 | 3 | yes | yes | 109 |
| v6 | 6 | gpt-5.5 | 60 | 60 | yes | yes | 112 |
| v6 | 6 | gpt-5.6-terra | 60 | 40 | no | yes | 111 |
| v6 | 7 | gpt-5.5 | 91 | 91 | yes | yes | 114 |
| v6 | 7 | gpt-5.6-terra | 91 | 91 | yes | yes | 113 |
| v6 | 8 | gpt-5.5 | 360 | 360 | yes | yes | 116 |
| v6 | 8 | gpt-5.6-terra | 360 | 120 | no | yes | 115 |
| v6 | 9 | gpt-5.5 | 8 | 8 | yes | yes | 118 |
| v6 | 9 | gpt-5.6-terra | 8 | 8 | yes | yes | 117 |
| v6 | 10 | gpt-5.5 | 34 | 34 | yes | yes | 120 |
| v6 | 10 | gpt-5.6-terra | 34 | 34 | yes | yes | 119 |
| v7 | 1 | gpt-5.5 | 18 | 18 | yes | yes | 122 |
| v7 | 1 | gpt-5.6-terra | 18 | 10 | no | yes | 121 |
| v7 | 2 | gpt-5.5 | 8 | 8 | yes | yes | 124 |
| v7 | 2 | gpt-5.6-terra | 8 | 8 | yes | yes | 123 |
| v7 | 3 | gpt-5.5 | 140 | 140 | yes | yes | 126 |
| v7 | 3 | gpt-5.6-terra | 140 | 140 | yes | yes | 125 |
| v7 | 4 | gpt-5.5 | 600 | 600 | yes | yes | 128 |
| v7 | 4 | gpt-5.6-terra | 600 | 600 | yes | yes | 127 |
| v7 | 5 | gpt-5.5 | 3 | 3 | yes | yes | 130 |
| v7 | 5 | gpt-5.6-terra | 3 | 3 | yes | yes | 129 |
| v7 | 6 | gpt-5.5 | 60 | 60 | yes | yes | 132 |
| v7 | 6 | gpt-5.6-terra | 60 | 40 | no | yes | 131 |
| v7 | 7 | gpt-5.5 | 91 | 91 | yes | yes | 134 |
| v7 | 7 | gpt-5.6-terra | 91 | 91 | yes | yes | 133 |
| v7 | 8 | gpt-5.5 | 360 | 360 | yes | yes | 136 |
| v7 | 8 | gpt-5.6-terra | 360 | 360 | yes | yes | 135 |
| v7 | 9 | gpt-5.5 | 8 | 8 | yes | yes | 138 |
| v7 | 9 | gpt-5.6-terra | 8 | 8 | yes | yes | 137 |
| v7 | 10 | gpt-5.5 | 34 | 34 | yes | yes | 140 |
| v7 | 10 | gpt-5.6-terra | 34 | 34 | yes | yes | 139 |
| v8 | 1 | gpt-5.5 | 18 | 18 | yes | no | 142 |
| v8 | 1 | gpt-5.6-terra | 18 | 10 | no | no | 141 |
| v8 | 2 | gpt-5.5 | 8 | 8 | yes | no | 144 |
| v8 | 2 | gpt-5.6-terra | 8 | 8 | yes | no | 143 |
| v8 | 3 | gpt-5.5 | 140 | 140 | yes | no | 146 |
| v8 | 3 | gpt-5.6-terra | 140 | 140 | yes | no | 145 |
| v8 | 4 | gpt-5.5 | 600 | 600 | yes | no | 148 |
| v8 | 4 | gpt-5.6-terra | 600 | 600 | yes | no | 147 |
| v8 | 5 | gpt-5.5 | 3 | 3 | yes | no | 150 |
| v8 | 5 | gpt-5.6-terra | 3 | 3 | yes | no | 149 |
| v8 | 6 | gpt-5.5 | 60 | 60 | yes | no | 152 |
| v8 | 6 | gpt-5.6-terra | 60 | 60 | yes | no | 151 |
| v8 | 7 | gpt-5.5 | 91 | 91 | yes | no | 154 |
| v8 | 7 | gpt-5.6-terra | 91 | 91 | yes | no | 153 |
| v8 | 8 | gpt-5.5 | 360 | 360 | yes | no | 156 |
| v8 | 8 | gpt-5.6-terra | 360 | 1440 | no | no | 155 |
| v8 | 9 | gpt-5.5 | 8 | 8 | yes | no | 158 |
| v8 | 9 | gpt-5.6-terra | 8 | 4 | no | no | 157 |
| v8 | 10 | gpt-5.5 | 34 | 34 | yes | no | 160 |
| v8 | 10 | gpt-5.6-terra | 34 | 34 | yes | no | 159 |
| v9 | 1 | gpt-5.5 | 18 | 18 | yes | no | 162 |
| v9 | 1 | gpt-5.6-terra | 18 | 10 | no | no | 161 |
| v9 | 2 | gpt-5.5 | 8 | 8 | yes | no | 164 |
| v9 | 2 | gpt-5.6-terra | 8 | 8 | yes | no | 163 |
| v9 | 3 | gpt-5.5 | 140 | 140 | yes | no | 166 |
| v9 | 3 | gpt-5.6-terra | 140 | 140 | yes | no | 165 |
| v9 | 4 | gpt-5.5 | 600 | 600 | yes | no | 168 |
| v9 | 4 | gpt-5.6-terra | 600 | 600 | yes | no | 167 |
| v9 | 5 | gpt-5.5 | 3 | 3 | yes | no | 170 |
| v9 | 5 | gpt-5.6-terra | 3 | 3 | yes | no | 169 |
| v9 | 6 | gpt-5.5 | 60 | 60 | yes | no | 172 |
| v9 | 6 | gpt-5.6-terra | 60 | 60 | yes | no | 171 |
| v9 | 7 | gpt-5.5 | 91 | 91 | yes | no | 174 |
| v9 | 7 | gpt-5.6-terra | 91 | 91 | yes | no | 173 |
| v9 | 8 | gpt-5.5 | 360 | 360 | yes | no | 176 |
| v9 | 8 | gpt-5.6-terra | 360 | 360 | yes | no | 175 |
| v9 | 9 | gpt-5.5 | 8 | 8 | yes | no | 178 |
| v9 | 9 | gpt-5.6-terra | 8 | 8 | yes | no | 177 |
| v9 | 10 | gpt-5.5 | 34 | 34 | yes | no | 180 |
| v9 | 10 | gpt-5.6-terra | 34 | 34 | yes | no | 179 |
