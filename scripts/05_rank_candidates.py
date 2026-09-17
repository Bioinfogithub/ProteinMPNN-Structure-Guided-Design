"""
Simple transparent candidate ranking.

This is only a baseline. A real study should combine ProteinMPNN metrics
with structure prediction, interface metrics, stability, developability,
and project-specific objectives.
"""
import pandas as pd
from pathlib import Path

def main():
    inp = Path("results/tables/candidate_metrics.csv")
    if not inp.exists():
        print(f"{inp} not found. Create a metrics table first.")
        return

    df = pd.read_csv(inp)

    # If these columns exist, normalize simple metrics for a baseline score.
    score = pd.Series(0.0, index=df.index)
    if "mpnn_score" in df:
        score += -df["mpnn_score"].rank(pct=True)
    if "identity" in df:
        score += df["identity"].rank(pct=True)
    if "num_substitutions" in df:
        score += df["num_substitutions"].rank(pct=True) * 0.25

    df["baseline_score"] = score
    df = df.sort_values("baseline_score", ascending=False)
    out = Path("results/tables/ranked_candidates.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
