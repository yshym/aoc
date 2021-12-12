from part1 import path_count, limited_time_dfs
from part2 import more_time_dfs
from utils import map_strs, read_str, run_tests


def parse_str(s):
    u, v = s.split("-")
    return (u, v)


INPUT = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
EDGES = map_strs(parse_str, read_str(INPUT))


def test_path_count():
    assert path_count(EDGES, limited_time_dfs) == 10


def test_more_time_path_count():
    assert path_count(EDGES, more_time_dfs) == 36


if __name__ == "__main__":
    run_tests(__name__)
