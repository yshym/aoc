from collections import deque

from utils import read_str


def three_increased_count(depths):
    depths = [int(d) for d in depths]
    dq = deque()
    wl = 3
    su = 0
    res = 0
    for d in depths[:wl]:
        dq.append(d)
        su += d
    for d in depths[wl:]:
        psu = su
        su = su - dq[0] + d
        res += psu < su
        dq.popleft()
        dq.append(d)
    return res


def three_increased_count_dp(depths):
    n = len(depths)
    depths = [int(d) for d in depths]
    wl = 3
    dp = [0] * n
    dp[0] = depths[0]
    res = 0
    for i in range(1, wl):
        dp[i] += dp[i - 1]
    for i in range(wl, n):
        dp[i] = dp[i - 1] - depths[i - 3] + depths[i]
        res += dp[i] > dp[i - 1]
    return res


def test_three_increased_count():
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
    depths = read_str(s)
    assert three_increased_count(depths) == 5
    assert three_increased_count_dp(depths) == 5


if __name__ == "__main__":
    test_three_increased_count()
