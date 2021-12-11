from copy import deepcopy

from part1 import flash_count
from part2 import first_simultaneous_flash
from utils import map_strs, read_str, run_tests


def parse_str(s):
    return map_strs(int, s)


INPUT = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
ENERGY_LEVELS = map_strs(parse_str, read_str(INPUT))


def test_flash_count():
    assert flash_count(deepcopy(ENERGY_LEVELS)) == 1656


def test_first_simultaneous_flash():
    assert first_simultaneous_flash(deepcopy(ENERGY_LEVELS)) == 195


if __name__ == "__main__":
    run_tests(__name__)
