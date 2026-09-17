# Workflow

## 1. Structure selection

Select an experimentally determined or predicted structure appropriate for the design question.

## 2. Design definition

Define:

- chains to redesign
- residues to redesign
- residues to keep fixed
- optional residue constraints or biases
- number of sequences and sampling temperatures

## 3. ProteinMPNN sequence generation

Run the official ProteinMPNN implementation on the prepared backbone.

ProteinMPNN supports fixed positions, multichain design, tied positions, amino-acid biases, and multiple sampling temperatures.

## 4. Sequence-level analysis

Compare generated sequences using:

- sequence identity
- substitutions
- amino-acid composition
- ProteinMPNN score
- diversity

## 5. Structural validation

Predict or assess structures for shortlisted sequences.

## 6. Functional prioritization

Depending on the project, assess:

- interface geometry
- binding interactions
- stability
- solubility/developability
- conformational dynamics

## 7. Experimental validation

Computational ranking is followed by experimental testing when appropriate.
