from typing import Callable, List, Union


def read_str(s: str) -> List[str]:
    return s.strip().split("\n")


def read_file(n: str) -> List[str]:
    with open(n, "r") as f:
        s = f.read()
    return read_str(s)


def map_strs(
    t: Callable[[str], Union[int, float]], strs
) -> List[Union[int, float]]:
    return list(map(t, strs))
