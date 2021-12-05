def overlapping_points_number(coords, count_diagonal=False):
    m = n = 0
    for (x1, y1), (x2, y2) in coords:
        m = max(m, x1 + 1, x2 + 1)
        n = max(n, y1 + 1, y2 + 1)
    matrix = [[0] * m for _ in range(n)]
    for (x1, y1), (x2, y2) in coords:
        if y1 == y2 or x1 == x2:
            (x1, x2), (y1, y2) = sorted([x1, x2]), sorted([y1, y2])
            r, c = y1, x1
            while y1 == y2 and c <= x2:
                matrix[r][c] += 1
                c += 1
            while x1 == x2 and r <= y2:
                matrix[r][c] += 1
                r += 1
            continue
        r, c = y1, x1
        while count_diagonal and ((y1 < y2) == (r < y2) or r == y2):
            matrix[r][c] += 1
            r += 1 if y1 < y2 else -1
            c += 1 if x1 < x2 else -1
    res = 0
    for r in range(n):
        for c, v in enumerate(matrix[r]):
            if v > 1:
                res += 1
    return res
