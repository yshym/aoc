from part1 import corrupted_lines_score
from part2 import incomplete_lines_middle_score
from utils import read_str, run_tests


INPUT = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""
LINES = read_str(INPUT)


def test_corrupted_lines():
    assert corrupted_lines_score(LINES) == 26397


def test_incomplete_lines_score():
    assert incomplete_lines_middle_score(LINES) == 288957


if __name__ == '__main__':
    run_tests(__name__)
