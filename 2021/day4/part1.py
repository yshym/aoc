def score(nums, boards, j=0):
    m, n = 5, len(boards)
    # [{value: (row, col)}, ...]
    vtis = [
        {v: (r, c) for r, row in enumerate(b) for c, v in enumerate(row)}
        for b in boards
    ]
    # [(0b11111, 0b11111), ...]
    rc_pairs = [([31] * m, [31] * m) for b in boards]
    playing = set(range(n))
    wi = lnum = None
    for num in nums:
        if wi:
            break
        for i in range(n):
            if i not in playing or num not in vtis[i]:
                continue
            r, c = vtis[i][num]
            rcp = rc_pairs[i]
            rcp[0][r] &= ~(1 << c)
            rcp[1][c] &= ~(1 << r)
            if 0 in {rcp[0][r], rcp[1][c]}:
                if len(playing) == n - j:
                    wi, lnum = i, num
                    break
                playing.discard(i)
    wb, rcp = boards[wi], rc_pairs[wi]
    us = 0
    for r in range(m):
        for c, v in enumerate(wb[r]):
            if not rcp[0][r] & 1 << c:
                continue
            us += v
    return us * lnum
