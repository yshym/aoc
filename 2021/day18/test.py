from part1 import snail_sum
from part2 import largest_magnitude
from utils import run_tests


def read_str(s):
    return [eval(x) for x in s.strip().split("\n")]


INPUT = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""
NUMS = read_str(INPUT)


def test_add():
    assert snail_sum(NUMS) == 4140


def test_largest_magnitude():
    assert largest_magnitude(NUMS) == 3993


if __name__ == "__main__":
    run_tests(__name__)
