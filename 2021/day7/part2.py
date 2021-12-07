def least_fuel_with_nonconstant_burning(positions):
    m, n = max(positions), len(positions)
    res = float("inf")
    for p in range(m):
        fuel = 0
        for j in range(n):
            if fuel > res:
                break
            diff = abs(positions[j] - p)
            mean = diff // 2 + (1 if diff % 2 else 0.5)
            fuel += int(mean * diff)
        res = min(res, fuel)
    return res
