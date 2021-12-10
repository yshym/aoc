from part1 import risk_level_sum
from part2 import basins_product
from utils import map_strs, run_tests


def read_str(s):
    heightmap = []
    for line in s.strip().split("\n"):
        heightmap.append(map_strs(int, line))
    return heightmap


INPUT = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""
HEIGHTMAP = read_str(INPUT)


def test_risk_level_sum():
    assert risk_level_sum(HEIGHTMAP)[0] == 15


def test_basins_product():
    assert basins_product(HEIGHTMAP) == 1134


if __name__ == "__main__":
    run_tests(__name__)
