def more_time_dfs(graph, u, small_visited, visited_twice=False):
    count = 0
    if u == "end":
        count += 1
        return count
    is_small = u.islower()
    became_visited_twice = False
    if is_small:
        if u in small_visited:
            visited_twice = True
            became_visited_twice = True
        else:
            small_visited.add(u)
    for v in graph[u]:
        if (
            v == "start"
            or v.islower()
            and v in small_visited
            and visited_twice
        ):
            continue
        count += more_time_dfs(graph, v, small_visited, visited_twice)
    if is_small:
        if became_visited_twice:
            visited_twice = False
        else:
            small_visited.discard(u)
    return count
