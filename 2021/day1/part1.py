def increased_count(depths):
    n = len(depths)
    res = 0
    for i in range(1, n):
        res += depths[i] > depths[i - 1]
    return res
