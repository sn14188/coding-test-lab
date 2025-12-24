# problem url: https://www.acmicpc.net/problem/1865

import sys

input = sys.stdin.readline


def solution():
    T = int(input())

    for tc in range(T):
        N, M, W = map(int, input().split())

        edges = []
        for _ in range(M):
            s, e, t = map(int, input().split())
            edges.append((s, e, t))
            edges.append((e, s, t))

        for _ in range(W):
            s, e, t = map(int, input().split())
            edges.append((s, e, -t))

        dist = [0] * (N + 1)

        for _ in range(N):
            for u, v, w in edges:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w

        negative_cycle = False
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                negative_cycle = True
                break

        if negative_cycle:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solution()
