from utils import read_str


def power_consumption(strs):
    m = len(strs[0])
    rates = [0] * m
    gamma = 0
    for s in strs:
        for i, c in enumerate(s):
            rates[i] += 1 if c == "1" else -1
    for i, r in enumerate(rates):
        if r > 0:
            gamma |= 1 << m - i - 1
    return gamma * (~gamma & (2 ** m - 1))


def test_power_consumption():
    s = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
    """
    strs = read_str(s)
    assert power_consumption(strs) == 198


if __name__ == "__main__":
    test_power_consumption()
