from part1 import score
from part2 import score_last
from utils import map_strs, run_tests


def read_str(s):
    numbers_str, boards_str = s.strip().split("\n\n", maxsplit=1)
    numbers = map_strs(int, numbers_str.split(","))
    grid_strs = boards_str.split("\n\n")
    boards = [
        [list(map(int, rs.strip().split())) for rs in gs.split("\n")]
        for gs in grid_strs
    ]
    return numbers, boards


INPUT = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
NUMS, BOARDS = read_str(INPUT)


def test_score():
    assert score(NUMS, BOARDS) == 4512


def test_score_last():
    assert score_last(NUMS, BOARDS) == 1924


if __name__ == "__main__":
    run_tests(__name__)
