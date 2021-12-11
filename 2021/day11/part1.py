def dfs(matrix, r, c, visited):
    n = len(matrix)
    count = 0
    directions = (1, -1, -1, 1, 1, 0, -1, 0, 1)
    flashed = False
    if matrix[r][c] > 9:
        count += 1
        matrix[r][c] = 0
        flashed = True
    visited.add((r, c))
    for i in range(8):
        nr, nc = r + directions[i], c + directions[i + 1]
        if 0 <= nr < n and 0 <= nc < n and matrix[nr][nc]:
            matrix[nr][nc] += flashed
            if (nr, nc) not in visited or matrix[nr][nc] > 9:
                count += dfs(matrix, nr, nc, visited)
    return count


def flash_count(energy_levels):
    n, k = 10, 100
    res = 0
    for _ in range(k):
        for r in range(n):
            for c in range(n):
                energy_levels[r][c] += 1
        res += dfs(energy_levels, 0, 0, set())
    return res
