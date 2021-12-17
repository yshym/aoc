from functools import reduce

from part1 import evaluate_expression
from part2 import versions_sum
from utils import run_tests


def read_str(s):
    return reduce(
        lambda acc, x: acc + list(f"{int(x, 16):04b}"), s.strip(), []
    )


INPUTS1 = [
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
]
VERSION_SUMS = [
    16,
    12,
    23,
    31,
]
TRANSMISSIONS1 = [read_str(i) for i in INPUTS1]
INPUTS2 = [
    "C200B40A82",
    "04005AC33890",
    "880086C3E88112",
    "CE00C43D881120",
    "D8005AC2A8F0",
    "F600BC2D8F",
    "9C005AC2F8F0",
    "9C0141080250320F1802104A08",
]
EXPRESSION_RESULTS = [
    3,
    54,
    7,
    9,
    1,
    0,
    0,
    1,
]
TRANSMISSIONS2 = [read_str(i) for i in INPUTS2]


def test_versions_sum():
    for t, s in zip(TRANSMISSIONS1, VERSION_SUMS):
        vsum = versions_sum(t)
        assert vsum == s, f"{vsum} != {s}"


def test_evaluate_expression():
    for t, r in zip(TRANSMISSIONS2, EXPRESSION_RESULTS):
        _, values, _ = evaluate_expression(t)
        assert values[0] == r, f"{values[0]} != {r}"


if __name__ == "__main__":
    run_tests(__name__)
