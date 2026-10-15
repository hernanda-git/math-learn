# Dataset management

Use the source repo in sparse mode:

```bash
cd C:/Workspace/math
git sparse-checkout init --cone
git sparse-checkout set preprints/The-Quasi-Riemann-Hypothesis-September-30-2026
git checkout
```

Configuration lives in `config/datasets.json`. The pipeline never writes to `math`.
