from part1 import lowest_total_risk


def lowest_total_risk_larger_cave(risk_levels):
    sm, sn = len(risk_levels), len(risk_levels[0])
    m, n = sm * 5, sn * 5
    larger_cave_risk_levels = [[None] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            br, bc = r // sm, c // sn
            v = risk_levels[r % sm][c % sn]
            nv = v if (br, bc) == (0, 0) else v + br + bc
            larger_cave_risk_levels[r][c] = 9 if nv == 9 else nv % 9
    return lowest_total_risk(larger_cave_risk_levels)
