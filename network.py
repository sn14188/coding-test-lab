# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/43162


def solution(n: int, computers: list[list[int]]) -> int:
    visited = [False] * n

    def bfs(start_node):
        queue = []
        queue.append(start_node)
        visited[start_node] = True

        while queue:
            curr = queue.pop(0)

            for other_computer in range(n):
                if (
                    computers[curr][other_computer] == 1
                    and visited[other_computer] == False
                ):
                    queue.append(other_computer)
                    visited[other_computer] = True

    answer = 0
    for computer in range(n):
        if visited[computer] == False:
            answer += 1
            bfs(computer)

    return answer


assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1

print("All tests passed!")
