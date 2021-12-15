from part1 import lowest_total_risk
from part2 import lowest_total_risk_larger_cave
from utils import map_strs, run_tests


def read_str(s):
    return map_strs(lambda l: map_strs(int, l), s.strip().split("\n"))


INPUT = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
RISK_LEVELS = read_str(INPUT)


def test_lowest_total_risk():
    assert lowest_total_risk(RISK_LEVELS) == 40


def test_lowest_total_risk_larger_cave():
    assert lowest_total_risk_larger_cave(RISK_LEVELS) == 315


if __name__ == "__main__":
    run_tests(__name__)
