def risk_level_sum(heightmap):
    m, n = len(heightmap), len(heightmap[0])
    directions = [0, 1, 0, -1, 0]
    res, low_points = 0, set()
    for r in range(m):
        for c, h in enumerate(heightmap[r]):
            is_low_point = True
            for i in range(4):
                nr, nc = r + directions[i], c + directions[i + 1]
                if 0 <= nr < m and 0 <= nc < n:
                    if heightmap[nr][nc] <= h:
                        is_low_point = False
            if is_low_point:
                low_points.add((r, c))
                res += h + 1
    return res, low_points
