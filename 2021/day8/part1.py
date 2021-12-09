def digit_count(strs):
    res = 0
    for s in strs:
        res += len(s) in {2, 4, 3, 7}
    return res
