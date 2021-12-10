def corrupted_lines_score(lines):
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    complements = {"(": ")", "[": "]", "{": "}", "<": ">"}
    res = 0
    for l in lines:
        stack = []
        for c in l:
            if c in {"(", "[", "{", "<"}:
                stack.append(c)
            else:
                if c != complements[stack[-1]]:
                    res += points[c]
                    break
                stack.pop()
    return res
