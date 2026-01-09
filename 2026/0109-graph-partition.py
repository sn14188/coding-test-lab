# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42842


def solution(n: int, wires: list[list[int]]) -> int:
    answer = float("inf")

    for i in range(len(wires)):
        graph = {key: [] for key in range(1, n + 1)}

        for j in range(len(wires)):
            if i == j:
                continue

            a, b = wires[j]

            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(tower):
            visited.add(tower)
            tower_count = 1

            for next_tower in graph[tower]:
                if next_tower not in visited:
                    tower_count += dfs(next_tower)

            return tower_count

        chunk_1_count = dfs(1)
        answer = min(answer, abs(chunk_1_count - (n - chunk_1_count)))

    return answer


assert (
    solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]) == 3
)
assert solution(4, [[1, 2], [2, 3], [3, 4]]) == 0
assert solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]) == 1

print("All tests passed!")
