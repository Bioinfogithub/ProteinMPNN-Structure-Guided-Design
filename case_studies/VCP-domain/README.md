# Case Study: VCP-DPBB Redesign

## Purpose

This folder documents how the structure-guided ProteinMPNN framework can be connected to the VCP-DPBB redesign work.

The broader workflow can be represented as:

```text
VCP-DPBB structure
        ↓
Conserved/interface residue analysis
        ↓
Define redesign positions
        ↓
ProteinMPNN sequence generation
        ↓
Sequence/property filtering
        ↓
Structure assessment
        ↓
Docking / interface analysis
        ↓
AAMD / CGMD
        ↓
Candidate prioritization
```

## What to add later

- VCP-DPBB structure information
- Reference sequence
- Designed positions
- ProteinMPNN settings
- Generated sequences
- Selected variants
- Structural/interface analysis
- MD and free-energy results

## Relationship to the broader project

This case study is particularly useful for showing how a structure-conditioned sequence-design model can fit into a larger computational protein-engineering workflow.

Do not present the case study as a ProteinMPNN-only result if other methods were also used. Clearly identify which step was performed by ProteinMPNN and which steps came from other design, docking, or simulation methods.
