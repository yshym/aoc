from itertools import permutations

from part1 import snail_sum


def largest_magnitude(nums):
    res = 0
    for pair in permutations(nums, 2):
        res = max(res, snail_sum(pair))
    return res
