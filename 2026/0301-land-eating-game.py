# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/12913


def solution(land: list[list[int]]):
    for i in range(1, len(land)):
        land[i][0] += max(land[i - 1][1], land[i - 1][2], land[i - 1][3])
        land[i][1] += max(land[i - 1][0], land[i - 1][2], land[i - 1][3])
        land[i][2] += max(land[i - 1][0], land[i - 1][1], land[i - 1][3])
        land[i][3] += max(land[i - 1][0], land[i - 1][1], land[i - 1][2])

    answer = max(land[-1])

    return answer


assert solution([[5, 1, 2, 3]]) == 5
assert solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]) == 16
assert solution([[100, 1, 1, 1], [100, 1, 1, 1], [100, 1, 1, 1]]) == 201

print("All tests passed!")
