"""Parse a simple FASTA file and report sequence lengths."""
from pathlib import Path
import argparse

def read_fasta(path):
    records = []
    name, seq = None, []
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if name is not None:
                records.append((name, "".join(seq)))
            name = line[1:].strip()
            seq = []
        else:
            seq.append(line)
    if name is not None:
        records.append((name, "".join(seq)))
    return records

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta")
    args = parser.parse_args()

    for name, seq in read_fasta(args.fasta):
        print(f"{name}\tlength={len(seq)}")

if __name__ == "__main__":
    main()
