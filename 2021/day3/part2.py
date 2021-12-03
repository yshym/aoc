def life_support_rating(strs):
    m = len(strs[0])
    rate = 0
    common = [[], []]
    cands = [strs, strs]
    for i in range(m):
        for j in range(2):
            if len(cands[j]) == 1:
                continue
            for s in cands[j]:
                b = int(s[i])
                rate += 1 if b else -1
                common[b].append(s)
            cands[j] = common[rate < 0] if j else common[rate >= 0]
            common = [[], []]
            rate = 0
    ogr, csr = [int(c, 2) for c in [cands[0][0], cands[1][0]]]
    return ogr * csr
