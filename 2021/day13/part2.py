def folded(dots, instructions):
    for ax, v in instructions:
        fold = (v, 0) if ax == "x" else (0, v)
        new_dots = set()
        for x, y in dots:
            fx, fy = fold
            if ax == "x" and x < fx or ax == "y" and y < fy:
                new_dots.add((x, y))
                continue
            nx, ny = x, y
            if ax == "x":
                diff = x - fx
                nx = fx - diff
            elif ax == "y":
                diff = y - fy
                ny = fy - diff
            new_dots.add((nx, ny))
        dots = new_dots
    mx = my = 0
    for x, y in dots:
        mx = max(mx, x)
        my = max(my, y)
    matrix = [[" "] * (mx + 1) for _ in range(my + 1)]
    for x, y in dots:
        matrix[y][x] = "#"
    return matrix
