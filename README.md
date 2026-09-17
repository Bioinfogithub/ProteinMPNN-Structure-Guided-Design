# ProteinMPNN Structure-Guided Protein Design

A simple and extensible computational workflow for **structure-guided protein sequence redesign using ProteinMPNN**.

This repository is intended as a research portfolio and a starting framework for exploring how a known protein structure can be used to generate and prioritize alternative amino-acid sequences.

## Overview

ProteinMPNN is a deep-learning-based inverse protein-design method that predicts amino-acid sequences compatible with a given protein backbone. It can be used for monomer design, multichain design, fixed-position design, tied positions, and sequence sampling at different temperatures.

This repository focuses on the **general workflow**, rather than presenting a fully optimized design pipeline.

```text
Input protein structure
        ↓
Structure preparation
        ↓
Define designable / fixed residues
        ↓
ProteinMPNN sequence generation
        ↓
Sequence filtering and comparison
        ↓
Structure prediction / validation
        ↓
Optional docking and molecular dynamics
        ↓
Candidate prioritization
        ↓
Experimental validation
```

## Main objectives

- Explore structure-guided protein sequence redesign.
- Demonstrate practical use of ProteinMPNN.
- Organize design inputs, generated sequences, and analysis in a reproducible manner.
- Compare designed sequences with the reference sequence.
- Provide a framework that can later be extended with AlphaFold/ESMFold, docking, MD, and machine-learning-based scoring.

## Repository structure

```text
ProteinMPNN-Structure-Guided-Design/
├── README.md
├── requirements.txt
├── environment.yml
├── .gitignore
│
├── data/
│   ├── README.md
│   └── design_config.yaml
│
├── scripts/
│   ├── 01_prepare_design.py
│   ├── 02_run_proteinmpnn.py
│   ├── 03_parse_sequences.py
│   ├── 04_compare_sequences.py
│   ├── 05_rank_candidates.py
│   └── run_pipeline.py
│
├── notebooks/
│   ├── 01_design_overview.ipynb
│   └── 02_sequence_analysis.ipynb
│
├── case_studies/
│   ├── Sotrovimab/
│   │   └── README.md
│   └── VCP-Domain/
│       └── README.md
│
├── results/
│   ├── sequences/
│   ├── figures/
│   └── tables/
│
└── docs/
    ├── workflow.md
    └── design_notes.md
```

## Case studies

Two case-study folders are included as **examples of how this framework can be used**:

### 1. Sotrovimab redesign

A structure-guided antibody redesign example can be used to study sequence changes around an antibody–antigen interface.

The folder is intentionally kept as a case-study framework rather than claiming new ProteinMPNN-generated results.

### 2. VCP-Domain redesign

The VCP project provides a relevant protein-domain redesign example involving structure-guided and AI-assisted sequence design.

The case-study folder is designed to document the workflow and connect ProteinMPNN with downstream structural and simulation-based analysis.

These examples can later be populated with actual structures, sequence files, design positions, generated sequences, and validated results.

## ProteinMPNN

The original ProteinMPNN implementation is available from the authors' repository:

https://github.com/dauparas/ProteinMPNN

ProteinMPNN performs the inverse-design task of finding amino-acid sequences compatible with a specified protein backbone. It supports fixed and designable residues, multichain systems, tied positions, amino-acid biases, and sampling at different temperatures.

For reproducible studies, record the ProteinMPNN version/commit, model checkpoint, random seed, sampling temperature, number of sequences, and designable positions.

## Basic usage

After installing ProteinMPNN, a typical command has the following conceptual form:

```bash
python protein_mpnn_run.py \
    --pdb_path input_structure.pdb \
    --pdb_path_chains A \
    --num_seq_per_target 32 \
    --sampling_temp "0.1 0.2 0.3" \
    --out_folder outputs/
```

The exact command should be adapted to the structure, chains, fixed positions, and design objective.

## Sequence analysis

The included Python scripts provide lightweight analysis for:

- sequence parsing
- sequence length
- identity to a reference sequence
- number of substitutions
- simple amino-acid composition
- candidate ranking using transparent baseline criteria

These scripts are deliberately simple so that the workflow can be modified for different projects.

## Suggested downstream validation

ProteinMPNN sequence generation should not be treated as experimental validation. A broader design workflow can include:

1. Structure prediction
2. Structural similarity assessment
3. Interface analysis
4. Protein–protein or protein–peptide docking, where appropriate
5. Molecular dynamics simulations
6. Binding/interface energy analysis
7. Experimental characterization

For example, AlphaFold/ESMFold can be used for structure assessment, while GROMACS or another MD package can be used for molecular dynamics.

## Reproducibility

For each design run, record:

- Input PDB / structure identifier
- Designed chains
- Fixed residues
- ProteinMPNN model
- Sampling temperature
- Number of sequences
- Random seed
- ProteinMPNN version or Git commit
- Downstream filtering criteria

## Important note

The scripts and example data in this repository are intended as a **general research framework and portfolio demonstration**. They should not be interpreted as experimentally validated designs.

Large files such as PDB trajectories, GROMACS trajectories, model weights, and other generated simulation files should generally not be committed to GitHub. Store them separately or use appropriate data repositories.

## References

Dauparas, J. et al. Robust deep learning–based protein sequence design using ProteinMPNN. *Science* 2022, 378, 49–56.

ProteinMPNN source code:
https://github.com/dauparas/ProteinMPNN

## Author

**Amar Jeet Yadav**  
Computational Biology | Protein Design | AI/ML | Molecular Modelling | Molecular Dynamics

IIT (BHU), Varanasi, India
