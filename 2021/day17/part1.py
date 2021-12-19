def launch_probe(square):
    (sx1, sy1), (sx2, sy2) = square
    x = y = 0
    hy = 0
    vc = 0

    def inside_square(x, y):
        return sx1 <= x <= sx2 and sy2 <= y <= sy1

    def passed_square(x, y):
        return x > sx2 or y < sy2

    for xv in range(sx2 + 1):
        if xv * (xv + 1) / 2 < sx1:
            continue
        abs_sy2 = abs(sy2)
        for yv in range(-abs_sy2, abs_sy2 + 1):
            tx, ty = x, y
            txv, tyv = xv, yv
            maxy = 0
            while True:
                if inside_square(tx, ty):
                    vc += 1
                    hy = max(hy, maxy)
                    break
                if passed_square(tx, ty):
                    break
                maxy = max(maxy, ty)
                tx += txv
                ty += tyv
                txv = max(0, txv - 1)
                tyv -= 1
    return hy, vc
