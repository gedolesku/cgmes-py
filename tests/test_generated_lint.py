import subprocess
import shutil
from generate_cgmes_project import generate_dataclasses


def test_generated_code_with_pylint():
    shutil.rmtree("generated", ignore_errors=True)
    """Run the generator and lint the result with pylint."""
    generate_dataclasses(
        "cgmes-models/v24/ENTSOE_CGMES_v2.4.15_7Aug2014.xml", "generated"
    )
    try:
        result = subprocess.run(
            ["pylint", "--errors-only", "generated"],
            capture_output=True,
            text=True,
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        assert result.returncode == 0, "pylint found errors"
    finally:
        pass
        # shutil.rmtree("generated", ignore_errors=True)
