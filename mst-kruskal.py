# problem url: https://www.acmicpc.net/problem/1197


import sys

input = sys.stdin.readline


def find(parent: list[int], x: int) -> int:
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x


def union(parent: list[int], a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)

    if a != b:
        parent[b] = a


def kruskal(v: int, edges: list[tuple[int, int, int]]) -> int:
    total = 0

    parent = [i for i in range(v + 1)]
    edges.sort(key=lambda x: x[2])

    for a, b, w in edges:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            total += w

    return total


def main() -> None:
    V, E = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(E)]

    print(kruskal(V, edges))


if __name__ == "__main__":
    main()
