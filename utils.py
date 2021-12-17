import sys
from inspect import getmembers, isfunction
from typing import Callable, List


def read_str(s: str) -> List[str]:
    return s.strip().split("\n")


def read_file(n: str) -> List[str]:
    with open(n) as f:
        s = f.read()
    return read_str(s)


def map_strs(f: Callable, strs: List[str]):
    return list(map(f, strs))


def run_tests(module_name: str):
    module = sys.modules[module_name]
    functions = getmembers(module, isfunction)
    for n, f in functions:
        if n.startswith("test"):
            f()
