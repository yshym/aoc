from functools import lru_cache, reduce


def lanternfish_count(fish, dc=80):
    n = len(fish)

    @lru_cache
    def helper(f, d):
        if d == -1:
            return 0
        if f >= 0:
            return helper(f - 1, d - 1)
        new = helper(8, d)
        return 1 + helper(6, d) + new

    return n + reduce(lambda acc, f: acc + helper(f, dc), fish, 0)
