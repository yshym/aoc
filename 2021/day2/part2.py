def course_with_aim(commands):
    hp = d = a = 0
    for c in commands:
        word, arg = c.split()
        num = int(arg)
        if word == "forward":
            hp += num
            d += a * num
        else:
            a += (1 if word == "down" else -1) * num
    return hp * d
