from part1 import dot_count
from part2 import folded
from utils import map_strs, run_tests


def read_str(s):
    dots_str, instructions_str = s.split("\n\n")
    dots = map_strs(
        lambda pair: map_strs(int, pair.split(",")),
        dots_str.strip().split("\n"),
    )
    instructions = []
    for s in instructions_str.strip().split("\n"):
        ax, v = s.split(" ")[-1].split("=")
        instructions.append((ax, int(v)))
    return dots, instructions


INPUT = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""
DOTS, INSTRUCTIONS = read_str(INPUT)


def test_dot_count_after_first_fold():
    assert dot_count(DOTS, INSTRUCTIONS) == 17


def test_folded():
    output = """
#####
#   #
#   #
#   #
#####
    """
    parsed_output = [list(s) for s in output.strip().split("\n")]
    assert folded(DOTS, INSTRUCTIONS) == parsed_output


if __name__ == "__main__":
    run_tests(__name__)
    folded(DOTS, INSTRUCTIONS)
