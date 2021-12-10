import heapq

from part1 import risk_level_sum


def basins_product(heightmap):
    _, low_points = risk_level_sum(heightmap)
    m, n = len(heightmap), len(heightmap[0])
    directions = [0, 1, 0, -1, 0]
    visited = set()
    bs = 0
    k = 3
    h = []
    res = 1

    def dfs(p):
        nonlocal bs
        bs += 1
        visited.add(tuple(p))
        r, c = p
        for i in range(4):
            nr, nc = r + directions[i], c + directions[i + 1]
            if (
                0 <= nr < m
                and 0 <= nc < n
                and (nr, nc) not in visited
                and heightmap[nr][nc] != 9
            ):
                dfs((nr, nc))

    for lp in low_points:
        dfs(lp)
        heapq.heappush(h, -bs)
        bs = 0
    while h and k:
        res *= -heapq.heappop(h)
        k -= 1
    return res
