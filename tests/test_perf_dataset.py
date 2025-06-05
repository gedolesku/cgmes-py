import os
import pytest

from benchmarks.perf import main


@pytest.mark.perf
def test_dataset_perf():
    if not os.environ.get("CGMES_BENCH_DIR"):
        pytest.skip("benchmark dataset not available")
    main()
