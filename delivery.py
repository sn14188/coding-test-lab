# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/12978


def solution(N: int, road: list[list[int]], K: int) -> int:
    graph = dict()
    for r in road:
        dep, arr, time = r[0], r[1], r[2]

        if dep not in graph:
            graph[dep] = [(arr, time)]
        else:
            graph[dep].append((arr, time))

        if arr not in graph:
            graph[arr] = [(dep, time)]
        else:
            graph[arr].append((dep, time))

    visited = [False] * (N + 1)
    dist = [float("inf")] * (N + 1)
    dist[1] = 0

    for _ in range(N):
        curr = -1
        min_dist = float("inf")

        for i in range(1, N + 1):
            if not visited[i] and dist[i] < min_dist:
                curr = i
                min_dist = dist[i]

        if curr == -1:
            break

        visited[curr] = True

        if curr in graph:
            for arr, time in graph[curr]:
                if dist[arr] > dist[curr] + time:
                    dist[arr] = dist[curr] + time

    answer = 0
    for d in dist:
        if d <= K:
            answer += 1

    return answer


assert (
    solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
    == 4
)
assert (
    solution(
        6,
        [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]],
        4,
    )
    == 4
)

print("All tests passed!")
