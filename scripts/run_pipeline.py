"""Run the lightweight preparation/analysis workflow."""
import subprocess
import sys

scripts = [
    "scripts/01_prepare_design.py",
    "scripts/02_run_proteinmpnn.py",
]

for script in scripts:
    print(f"\n>>> Running {script}")
    subprocess.run([sys.executable, script], check=True)
