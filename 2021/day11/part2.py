from part1 import dfs


def first_simultaneous_flash(energy_levels):
    n = 10
    res = 0
    i = 1
    prev_res = res
    while True:
        for r in range(n):
            for c in range(n):
                energy_levels[r][c] += 1
        res += dfs(energy_levels, 0, 0, set())
        if res - prev_res == n ** 2:
            return i
        i += 1
        prev_res = res
    return res
