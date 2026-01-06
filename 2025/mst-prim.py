# problem url: https://www.acmicpc.net/problem/1197


import sys
import heapq

input = sys.stdin.readline


def prim(v: int, graph: list[list[tuple[int, int]]]) -> int:
    total = 0
    visited = [False] * (v + 1)

    heap: list[tuple[int, int]] = [(0, 1)]

    while heap:
        w, u = heapq.heappop(heap)

        if visited[u]:
            continue

        visited[u] = True
        total += w

        for nxt, cost in graph[u]:
            if not visited[nxt]:
                heapq.heappush(heap, (cost, nxt))

    return total


def main() -> None:
    V, E = map(int, input().split())
    graph: list[list[tuple[int, int]]] = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    print(prim(V, graph))


if __name__ == "__main__":
    main()
