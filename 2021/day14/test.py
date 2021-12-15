from part1 import score
from part2 import score_after_40_steps
from utils import map_strs, run_tests


def read_str(s):
    template_str, rules_str = s.strip().split("\n\n")
    template = template_str.strip()
    rules = map_strs(
        lambda s: tuple(s.split(" -> ")), rules_str.strip().split("\n")
    )
    return template, rules


INPUT = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""
TEMPLATE, RULES = read_str(INPUT)


def test_score_after_10_steps():
    assert score(TEMPLATE, RULES, 10) == 1588


def test_score_after_40_steps():
    assert score_after_40_steps(TEMPLATE, RULES) == 2188189693529


if __name__ == "__main__":
    run_tests(__name__)
