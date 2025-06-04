import subprocess
import shutil
from pathlib import Path


def test_generated_code_with_ruff():
    """Run the generator and lint the result with ruff."""
    subprocess.run(["python", "generate_cgmes_project.py"], check=True)
    try:
        result = subprocess.run(
            ["ruff", "check", "generated", "--exit-zero"],
            capture_output=True,
            text=True,
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        assert result.returncode == 0, "ruff did not run successfully"
    finally:
        shutil.rmtree("generated", ignore_errors=True)

