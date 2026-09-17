# Design Notes

## Scope

This repository is deliberately broader and simpler than a fully project-specific protein-design pipeline.

## ProteinMPNN metrics

ProteinMPNN reports quantities such as sequence/design scores and can generate multiple sequence samples at different temperatures. These metrics should be interpreted in the context of the design problem rather than treated as direct predictions of experimental stability or affinity.

## Candidate prioritization

A practical design campaign can combine:

- ProteinMPNN sequence compatibility
- sequence diversity
- predicted structural confidence
- interface quality
- stability/developability
- molecular simulation results

The weighting of these criteria should be defined by the scientific objective.

## Future extensions

Possible additions include:

- AlphaFold/ESMFold validation
- interface-aware redesign
- Rosetta/FoldX stability analysis
- docking
- AAMD/CGMD
- free-energy calculations
- ML-based property prediction
- multi-objective optimization
