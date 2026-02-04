# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/49189


def solution(n: int, edge: list[list[int]]) -> int:
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    distance = [-1] * (n + 1)
    distance[1] = 0

    queue = []
    queue.append(1)

    while queue:
        curr = queue.pop(0)

        for next_node in graph[curr]:
            if distance[next_node] == -1:
                distance[next_node] = distance[curr] + 1
                queue.append(next_node)

    max_distance = max(distance)
    answer = distance.count(max_distance)

    return answer


assert solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]) == 3

print("All tests passed!")
