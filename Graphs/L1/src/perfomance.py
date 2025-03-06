import time
import typing as tp


P = tp.ParamSpec("P")
T = tp.TypeVar("T")


def get_average_exec_time(
    func: tp.Callable[P, T],
    *args: P.args,
    **kwargs: P.kwargs,
) -> float:
    total_time = 0.0

    for _ in range(100_000):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()

        total_time += end_time - start_time

    return total_time / 100_000
