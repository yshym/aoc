def power_consumption(strs):
    m = len(strs[0])
    rates = [0] * m
    gamma = 0
    for s in strs:
        for i, c in enumerate(s):
            rates[i] += 1 if c == "1" else -1
    for i, r in enumerate(rates):
        if r > 0:
            gamma |= 1 << m - i - 1
    return gamma * (~gamma & (2 ** m - 1))
