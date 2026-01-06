import math


def solution(info: list[str], start: str) -> list[int]:
    edges = []
    vertices = set()
    for line in info:
        u, v, w_str = line.split()
        edges.append((u, v, int(w_str)))
        vertices.add(u)
        vertices.add(v)

    dist = {vertex: math.inf for vertex in vertices}
    dist[start] = 0

    n = len(vertices)
    for _ in range(n - 1):
        for edge in edges:
            u, v, w = edge
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return [-1]

    answer = [dist[vertex] for vertex in sorted(vertices) if vertex != start]

    return answer


assert solution(["A B 4", "A C 3", "B C -1", "C A -2"], "A") == [4, 3]
assert solution(["A B 4", "A C 3", "B C -4", "C A -2"], "A") == [-1]

print("All tests passed!")
