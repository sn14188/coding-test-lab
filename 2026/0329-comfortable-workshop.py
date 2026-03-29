# problem url: https://www.codetree.ai/ko/frequent-problems/hsat/problems/easy-workshop/description


def solution(N: int, K: int, grid: list[list[int]]) -> int:
    answer = 0
    return answer


assert solution(4, 3, [[6, 7, 8, 1], [9, 1, 1, 1], [1, 1, 4, 8], [1, 1, 1, 9]]) == 1
assert (
    solution(
        5,
        4,
        [
            [16, 57, 98, 11, 52],
            [49, 61, 71, 31, 39],
            [51, 41, 54, 88, 93],
            [71, 21, 31, 41, 20],
            [48, 34, 22, 50, 44],
        ],
    )
    == 10
)

print("All tests passed!")
