# problem url: https://www.acmicpc.net/problem/5639


def solution(nums: list[int]) -> list[int]:
    if not nums:
        return []

    root = nums[0]
    rest = nums[1:]

    left = []
    right = []

    for num in rest:
        if num < root:
            left.append(num)
        else:
            right.append(num)

    return solution(left) + solution(right) + [root]


assert solution([]) == []
assert solution([50]) == [50]
assert solution([50, 60]) == [60, 50]
assert solution([50, 30, 24, 5]) == [
    5,
    24,
    30,
    50,
]
assert solution([50, 30, 24, 5, 28, 45]) == [
    5,
    28,
    24,
    45,
    30,
    50,
]
assert solution([50, 30, 24, 5, 28, 45, 98, 52, 60]) == [
    5,
    28,
    24,
    45,
    30,
    60,
    52,
    98,
    50,
]

print("All tests passed!")
