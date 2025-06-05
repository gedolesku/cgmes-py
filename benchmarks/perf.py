"""Run all performance benchmarks and enforce thresholds."""

from __future__ import annotations

from .bench_dataset import bench


THRESHOLD = 400_000  # objects per second


def main() -> None:
    thr = bench()
    if thr < THRESHOLD:
        raise SystemExit(f"dataset throughput {thr:.0f} < {THRESHOLD} obj/s")
    print(f"dataset throughput: {thr:.0f} obj/s")


if __name__ == "__main__":
    main()
