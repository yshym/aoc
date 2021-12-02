from utils import read_str


def course(commands):
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


def test_course():
    s = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
    """
    commands = read_str(s)
    assert course(commands) == 900


if __name__ == "__main__":
    test_course()
