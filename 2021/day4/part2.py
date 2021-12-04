from part1 import score


def score_last(nums, boards):
    n = len(boards)
    return score(nums, boards, n - 1)
