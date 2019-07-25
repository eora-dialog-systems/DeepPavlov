from typing import Callable, Union, NamedTuple

UserId = Union[str, int]


class SkillResponse(NamedTuple):
    response: str
    confidence: float


def expand_arguments(func: Callable):
    if func.__code__.co_argcount == 0:
        return lambda msg, context: func()
    elif func.__code__.co_argcount == 1:
        return lambda msg, context: func(msg)
    else:
        return func

