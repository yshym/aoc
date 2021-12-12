from collections import defaultdict


def limited_time_dfs(graph, u, small_visited):
    count = 0
    if u == "end":
        count += 1
        return count
    is_small = u.islower()
    if is_small:
        small_visited.add(u)
    for v in graph[u]:
        if v.islower() and v in small_visited:
            continue
        count += limited_time_dfs(graph, v, small_visited)
    if is_small:
        small_visited.discard(u)
    return count


def path_count(edges, dfs):
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    return dfs(graph, "start", set())
