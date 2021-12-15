from heapq import heappop, heappush


def lowest_total_risk(risk_levels):
    m, n = len(risk_levels), len(risk_levels[0])
    h, visited, costs = [(0, (0, 0))], set(), {(0, 0): 0}
    directions = [0, 1, 0, -1, 0]
    while h:
        cost, u = heappop(h)
        if u in visited:
            continue
        visited.add(u)
        if u == (m - 1, n - 1):
            return cost
        r, c = u
        for i in range(4):
            nr, nc = r + directions[i], c + directions[i + 1]
            if not (0 <= nr < m and 0 <= nc < n):
                continue
            v = (nr, nc)
            if v in visited:
                continue
            prev_cost = costs.get(v, float("inf"))
            new_cost = cost + risk_levels[nr][nc]
            if new_cost < prev_cost:
                costs[v] = new_cost
                heappush(h, (new_cost, v))
    return float("inf")
