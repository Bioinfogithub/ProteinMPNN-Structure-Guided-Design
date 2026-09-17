"""
Prepare a simple design configuration summary.

This script does not modify a PDB. It provides a lightweight starting point
for recording design choices before running ProteinMPNN.
"""
from pathlib import Path
import yaml

CONFIG = Path("data/design_config.yaml")

def main():
    if not CONFIG.exists():
        raise FileNotFoundError(f"Missing {CONFIG}")

    config = yaml.safe_load(CONFIG.read_text())
    print("ProteinMPNN design configuration")
    print("--------------------------------")
    for key, value in config.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
