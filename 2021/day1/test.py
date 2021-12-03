from part1 import increased_count
from part2 import three_increased_count, three_increased_count_dp
from utils import map_strs, read_str, run_tests


INPUT = """
199
200
208
210
200
207
240
269
260
263
"""
DEPTHS = map_strs(int, read_str(INPUT))


def test_increased_count():
    assert increased_count(DEPTHS) == 7


def test_three_increased_count():
    assert three_increased_count(DEPTHS) == 5
    assert three_increased_count_dp(DEPTHS) == 5


if __name__ == "__main__":
    run_tests(__name__)
