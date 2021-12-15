from collections import defaultdict, Counter


def score(template, rules, k):
    n = len(template)
    pairs = defaultdict(lambda: 0)
    pair_to_element = {tuple(r[0]): r[1] for r in rules}
    counter = Counter(template[-1])
    for i in range(1, n):
        e1, e2 = template[i - 1], template[i]
        pairs[(e1, e2)] += 1
    for i in range(k):
        new_pairs = defaultdict(lambda: 0)
        for p, c in pairs.items():
            e1, e2 = p
            new = pair_to_element[p]
            counter[new] += c
            new_pairs[(e1, new)] += c
            new_pairs[(new, e2)] += c
        pairs = new_pairs
    most_common = counter.most_common()
    return most_common[0][1] - most_common[-1][1]
