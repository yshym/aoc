def least_fuel(positions):
    n = len(positions)
    positions.sort()
    mi = positions[n // 2 - (n % 2 == 0)]
    res = 0
    for p in positions:
        res += abs(p - mi)
    return res
