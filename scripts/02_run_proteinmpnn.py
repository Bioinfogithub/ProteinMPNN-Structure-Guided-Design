"""
Print a ProteinMPNN command template.

The script intentionally does not execute ProteinMPNN because the official
ProteinMPNN source code/model weights are not bundled in this repository.
"""
def main():
    command = r"""
python protein_mpnn_run.py \
    --pdb_path input_structure.pdb \
    --pdb_path_chains A \
    --num_seq_per_target 32 \
    --sampling_temp "0.1 0.2 0.3" \
    --out_folder outputs/
"""
    print("ProteinMPNN command template:")
    print(command)

if __name__ == "__main__":
    main()
