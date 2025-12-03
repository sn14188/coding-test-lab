import math


def solution(info: list[str]) -> list[int]:
    edges = []
    nodes = set()
    for line in info:
        u, v, w_str = line.split()
        edges.append((u, v, int(w_str)))
        nodes.add(u)
        nodes.add(v)

    dist = {node: math.inf for node in nodes}
    prev = {node: None for node in nodes}
    dist["A"] = 0
    prev["A"] = "A"

    n = len(nodes)
    for _ in range(n - 1):
        for edge in edges:
            u, v, w = edge
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return [-1]

    answer = [dist[node] for node in sorted(nodes) if node != "A"]

    return answer


assert solution(["A B 4", "A C 3", "B C -1", "C A -2"]) == [4, 3]
assert solution(["A B 4", "A C 3", "B C -4", "C A -2"]) == [-1]

print("All tests passed!")
