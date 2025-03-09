import logging
from dataclasses import dataclass
from functools import wraps
from typing import (
    ParamSpec,
    TypeVar,
    Callable,
    Union,
    overload,
)


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class Count:
    cnt: int = 0

    def inc(self) -> None:
        self.cnt += 1

    def dec(self) -> None:
        self.cnt -= 1


P = ParamSpec("P")
T = TypeVar("T")


class TraceMacker:
    def __init__(
        self,
        sep: str = "*",
        size: int = 1,
    ) -> None:
        self.sep = sep
        self.size = size

    def __call__(self, func: Callable[P, T]) -> Callable[P, T]:
        count = Count()

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            count.inc()
            logger.info(
                "%s call func %r with args %s and kwargs %s",
                self.sep * count.cnt * self.size,
                func.__name__,
                args,
                kwargs,
            )
            res = func(*args, **kwargs)
            count.dec()
            logger.info(
                "%s call func %r got resuts %s",
                self.sep * count.cnt * self.size,
                func.__name__,
                res,
            )
            return res

        return wrapper


@overload
def trace(
    func: Callable[P, T] | None = None,
) -> Callable[P, T]: ...


@overload
def trace(
    *,
    sep: str = "*",
    size: int = 1,
) -> Callable[[Callable[P, T]], Callable[P, T]]: ...


def trace(
    func: Callable[P, T] | None = None,
    *,
    sep: str = "*",
    size: int = 1,
) -> Union[
    Callable[[Callable[P, T]], Callable[P, T]],
    Callable[P, T],
]:
    trace_maker = TraceMacker(sep=sep, size=size)

    if func is not None:
        return trace_maker(func=func)

    return trace_maker
