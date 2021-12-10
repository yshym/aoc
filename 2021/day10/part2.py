def incomplete_lines_middle_score(lines):
    points = {")": 1, "]": 2, "}": 3, ">": 4}
    complements = {"(": ")", "[": "]", "{": "}", "<": ">"}
    scores = []
    for l in lines:
        stack = []
        for c in l:
            if c in {"(", "[", "{", "<"}:
                stack.append(c)
            else:
                if c != complements[stack[-1]]:
                    stack = []
                    break
                stack.pop()
        if not stack:
            continue
        score = 0
        while stack:
            score = score * 5 + points[complements[stack.pop()]]
        scores.append(score)
    return sorted(scores)[len(scores) // 2]
