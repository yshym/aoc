from utils import map_strs, read_str


def increased_count(depths):
    n = len(depths)
    res = 0
    for i in range(1, n):
        res += depths[i] > depths[i - 1]
    return res


def test_increased_count():
    s = """
199
200
208
210
200
207
240
269
260
263
    """
    depths = map_strs(int, read_str(s))
    assert increased_count(depths) == 7


if __name__ == "__main__":
    test_increased_count()