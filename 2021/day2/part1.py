def course(commands):
    hp = d = 0
    for c in commands:
        word, arg = c.split()
        num = int(arg)
        if word == "forward":
            hp += num
        else:
            d += (1 if word == "down" else -1) * num
    return hp * d
