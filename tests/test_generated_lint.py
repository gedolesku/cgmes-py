from pathlib import Path
import subprocess
from generate_cgmes_project import generate_dataclasses


def test_generated_code_with_ruff():
    """Run the generator and lint the result with ruff."""
    # Call generate function directly instead of via subprocess
    generate_dataclasses("cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml", "generated")

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

