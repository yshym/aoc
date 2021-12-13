from part2 import folded


def dot_count(dots, instructions):
    paper = folded(dots, instructions[:1])
    return sum(
        [v == "#" for r in range(len(paper)) for _, v in enumerate(paper[r])]
    )
