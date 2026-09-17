"""Compare designed sequences with a reference sequence."""
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
            name, seq = line[1:].strip(), []
        else:
            seq.append(line)
    if name is not None:
        records.append((name, "".join(seq)))
    return records

def identity(ref, seq):
    n = min(len(ref), len(seq))
    if n == 0:
        return 0.0
    return sum(a == b for a, b in zip(ref[:n], seq[:n])) / n

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", required=True)
    parser.add_argument("--designs", required=True)
    args = parser.parse_args()

    ref = read_fasta(args.reference)[0][1]
    for name, seq in read_fasta(args.designs):
        ident = identity(ref, seq)
        print(f"{name}\tidentity={ident:.3f}\tsubstitutions_approx={int(round((1-ident)*min(len(ref), len(seq))))}")

if __name__ == "__main__":
    main()
