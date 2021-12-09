from functools import reduce
from typing import List

from part1 import digit_count
from part2 import values_sum
from utils import map_strs, read_str, run_tests


def parse_str(s):
    return s.split("|")[1].strip().split(" ")


def parse_str_as_pair(s):
    return tuple(x.split(" ") for x in s.split(" | "))


INPUT = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""
STRS: List[str] = list(
    reduce(lambda acc, v: acc + v, map_strs(parse_str, read_str(INPUT)), [])
)
PAIRS = map_strs(parse_str_as_pair, read_str(INPUT))


def test_digit_count():
    assert digit_count(STRS) == 26


def test_values_sum():
    assert values_sum(PAIRS) == 61229


if __name__ == "__main__":
    run_tests(__name__)
