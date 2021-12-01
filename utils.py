def read_str(s):
    return s.rstrip().split()


def read_file(n):
    with open(n, "r") as f:
        s = f.read()
    return read_str(s)
