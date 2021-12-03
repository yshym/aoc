from utils import read_str


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


def test_life_support_rating():
    s = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
    """
    strs = read_str(s)
    assert life_support_rating(strs) == 230


if __name__ == "__main__":
    test_life_support_rating()
