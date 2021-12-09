from collections import defaultdict


def patterns_to_mapping(patterns):
    length_to_segments = defaultdict(lambda: set("abcdefg"))
    for pattern in patterns:
        length_to_segments[len(pattern)] &= set(pattern)
    mapping = {}
    mapping["a"] = min(length_to_segments[3] - length_to_segments[2])
    mapping["g"] = min(
        length_to_segments[5] - ({mapping["a"]} | length_to_segments[4])
    )
    mapping["d"] = min(length_to_segments[5] - {mapping["a"], mapping["g"]})
    mapping["b"] = min(
        length_to_segments[4] - ({mapping["d"]} | length_to_segments[3])
    )
    mapping["f"] = min(length_to_segments[6] - {mapping[s] for s in "abdg"})
    mapping["c"] = min(length_to_segments[4] - {mapping[s] for s in "bdf"})
    mapping["e"] = min(length_to_segments[7] - {mapping[s] for s in "abcdfg"})
    return dict(zip(mapping.values(), mapping.keys()))


def values_sum(pairs):
    key_to_digit = {
        0b1110111: 0,
        0b0100100: 1,
        0b1011101: 2,
        0b1101101: 3,
        0b0101110: 4,
        0b1101011: 5,
        0b1111011: 6,
        0b0100101: 7,
        0b1111111: 8,
        0b1101111: 9,
    }
    res = 0
    for pair in pairs:
        patterns, values = pair
        mapping = patterns_to_mapping(patterns)
        num = 0
        for i, value in enumerate(values):
            value_segments = tuple(mapping[s] for s in value)
            key = 0
            for s in value_segments:
                key |= 1 << (ord(s) - ord("a"))
            digit = key_to_digit[key]
            num += digit * 10 ** (len(values) - (i + 1))
        res += num
    return res
