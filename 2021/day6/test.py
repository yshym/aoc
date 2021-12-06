from part1 import lanternfish_count
from part2 import lanternfish_count_256
from utils import map_strs, run_tests


def read_str(s):
    return s.strip().split(",")


INPUT = "3,4,3,1,2"
FISH = map_strs(int, read_str(INPUT))


def test_lanternfish_count():
    assert lanternfish_count(FISH) == 5934


def test_lanternfish_count_256():
    assert lanternfish_count_256(FISH) == 26984457539


if __name__ == "__main__":
    run_tests(__name__)
