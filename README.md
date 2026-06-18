# Fast Gemma TPS Smoke

Pinned to the Fast Gemma dashboard contract:

- upstream: https://huggingface.co/spaces/gemma-challenge/gemma-dashboard
- revision: 563325d19deaf6b3fc61f5a4e4915f0a6b004128

The smoke harness is CPU-safe and writes `score.json` with TPS/PPL fields.
Full A10G/GPU scoring can be enabled later by replacing `scripts/benchmark.py`
with a runner that preserves the same output schema.

```bash
python3 scripts/benchmark.py
cat score.json
```
