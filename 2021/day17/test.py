from part1 import launch_probe
from part2 import velocity_count
from utils import map_strs, run_tests


def read_str(s):
    xs, ys = s.strip().lstrip("target area: ").split(", ")
    (x1, x2), (y2, y1) = [
        map_strs(int, axs.split("=")[1].split("..")) for axs in (xs, ys)
    ]
    return (x1, y1), (x2, y2)


INPUT = "target area: x=20..30, y=-10..-5"
SQUARE = read_str(INPUT)


def test_highest_y():
    assert launch_probe(SQUARE)[0] == 45

def test_velocity_count():
    assert velocity_count(SQUARE) == 112


if __name__ == "__main__":
    run_tests(__name__)
