#!/usr/bin/env python3
import json, math, pathlib

root = pathlib.Path(__file__).resolve().parents[1]
cfg = json.loads((root / "submission.json").read_text())
tokens = float(cfg.get("tokensPerBatch", 128))
latency = max(1.0, float(cfg.get("latencyMs", 150)))
penalty = max(0.0, float(cfg.get("pplPenalty", 0.0)))
tps = tokens * 1000.0 / latency
ppl = 11.8 + penalty + max(0.0, 128.0 - tokens) / 512.0
valid = math.isfinite(tps) and math.isfinite(ppl) and ppl <= 25.0
score = tps if valid else 0.0
out = {
    "score": round(score, 4),
    "tps": round(tps, 4),
    "ppl": round(ppl, 4),
    "valid": bool(valid),
    "status": "smoke" if valid else "guardrail_failed",
    "method": cfg.get("model", "gemma-smoke-baseline"),
    "metrics": {"tokens": tokens, "latencyMs": latency},
}
(root / "score.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, sort_keys=True))
