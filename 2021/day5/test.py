from part1 import overlapping_points_number
from part2 import overlapping_points_number_with_diagonal
from utils import map_strs, read_str, run_tests


def parse_str(s):
    p1, p2 = s.split(" -> ")
    return tuple(tuple(map(int, p.split(","))) for p in (p1, p2))


INPUT = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
COORDS = map_strs(parse_str, read_str(INPUT))


def test_overlapping_points_number():
    assert overlapping_points_number(COORDS) == 5


def test_overlapping_points_number_with_diagonal():
    assert overlapping_points_number_with_diagonal(COORDS) == 12


if __name__ == "__main__":
    run_tests(__name__)
