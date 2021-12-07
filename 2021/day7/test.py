from part1 import least_fuel
from part2 import least_fuel_with_nonconstant_burning
from utils import map_strs, run_tests


def read_str(s):
    return s.strip().split(",")


INPUT = "16,1,2,0,4,2,7,1,2,14"
POSITIONS = map_strs(int, read_str(INPUT))


def test_least_fuel():
    assert least_fuel(POSITIONS) == 37


def test_least_fuel_with_nonconstant_burning():
    assert least_fuel_with_nonconstant_burning(POSITIONS) == 168


if __name__ == "__main__":
    run_tests(__name__)
