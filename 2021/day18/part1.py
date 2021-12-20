from functools import reduce
from math import ceil, floor


SPLIT = EXPLODE = True


def is_regular(num):
    return isinstance(num, int)


def has_nested_pair(num, level=0):
    if is_regular(num):
        return False
    if level == 4:
        return True
    for pair in num:
        if has_nested_pair(pair, level + 1):
            return True
    return False


def has_10_or_greater(num):
    if is_regular(num):
        return num >= 10
    for pair in num:
        if has_10_or_greater(pair):
            return True
    return False


def flattened(num):
    return [num] if is_regular(num) else sum(map(flattened, num), [])


def exploded(num):
    flattened_num = flattened(num)
    # (explode i, (left i, num to add), (right i, num to add))
    to_explode = (-1, (-1, 0), (-1, 0))
    n = len(flattened_num)
    i = 0

    def explore(num, level=0):
        global EXPLODE
        nonlocal to_explode
        nonlocal i
        if is_regular(num):
            i += 1
            return
        if (
            level >= 4
            and EXPLODE
            and is_regular(num[0])
            and is_regular(num[1])
        ):
            to_explode = (
                i,
                (i - 1, num[0]) if i - 1 >= 0 else None,
                (i + 2, num[1]) if i + 2 < n else None,
            )
            EXPLODE = False
        for pair in num:
            explore(pair, level + 1)

    def did_explode(num, level=0):
        nonlocal i
        nonlocal to_explode
        if is_regular(num):
            _, l, r = to_explode
            if l is not None and i == l[0]:
                num += l[1]
            elif r is not None and i == r[0]:
                num += r[1]
            i += 1
            return num
        if i == to_explode[0] and level == 4:
            i += 2
            return 0
        return [did_explode(pair, level + 1) for pair in num]

    explore(num)
    i = 0
    return did_explode(num)


def splitted(num):
    global SPLIT
    if is_regular(num):
        if num >= 10 and SPLIT:
            SPLIT = False
            return [floor(num / 2), ceil(num / 2)]
        return num
    return [splitted(pair) for pair in num]


def snail_reduced(num):
    global SPLIT, EXPLODE
    while True:
        if has_nested_pair(num):
            num = exploded(num)
            EXPLODE = True
        elif has_10_or_greater(num):
            num = splitted(num)
            SPLIT = True
        else:
            break
    return num


def magnitude(num):
    return (
        num
        if is_regular(num)
        else 3 * magnitude(num[0]) + 2 * magnitude(num[1])
    )


def snail_sum(nums):
    return magnitude(
        reduce(lambda acc, num: snail_reduced([acc, num]), nums[1:], nums[0])
    )
