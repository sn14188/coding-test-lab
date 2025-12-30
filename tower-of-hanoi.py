# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/12946


def solution(n: int) -> list[list[int]]:
    answer = []

    def dfs(n, start, mid, end):
        if n == 1:
            answer.append([start, end])
            return

        dfs(n - 1, start, end, mid)
        answer.append([start, end])
        dfs(n - 1, mid, start, end)

    dfs(n, 1, 2, 3)

    return answer


assert solution(2) == [[1, 2], [1, 3], [2, 3]]
assert solution(1) == [[1, 3]]
assert solution(3) == [[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]

print("All tests passed!")
