from part1 import course
from part2 import course_with_aim
from utils import read_str, run_tests


INPUT = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""
COMMANDS = read_str(INPUT)


def test_course():
    assert course(COMMANDS) == 150


def test_course_with_aim():
    assert course_with_aim(COMMANDS) == 900


if __name__ == "__main__":
    run_tests(__name__)
