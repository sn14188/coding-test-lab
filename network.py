# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/43162


def solution(n: int, computers: list[list[int]]) -> int:
    assert n == len(computers)

    answer = 0
    return answer


assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1

print("All tests passed!")
