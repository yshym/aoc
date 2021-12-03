from part1 import power_consumption
from part2 import life_support_rating
from utils import read_str, run_tests


INPUT = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
STRS = read_str(INPUT)


def test_power_consumption():
    assert power_consumption(STRS) == 198


def test_life_support_rating():
    assert life_support_rating(STRS) == 230


if __name__ == "__main__":
    run_tests(__name__)
