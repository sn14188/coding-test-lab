# problem url: https://www.acmicpc.net/problem/1806


def solution(numbers: list[int], target: int) -> int:
    start_idx, end_idx = 0, 0
    min_length = float("inf")

    while end_idx < len(numbers):
        partial_sum = sum(numbers[start_idx : end_idx + 1])

        if partial_sum < target:
            end_idx += 1
        else:
            while partial_sum >= target and start_idx <= end_idx:
                min_length = min(min_length, end_idx - start_idx + 1)
                start_idx += 1
                partial_sum = sum(numbers[start_idx : end_idx + 1])

    if min_length == float("inf"):
        return 0

    return min_length


assert solution([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 55) == 0
assert solution([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 15) == 2
assert solution([5, 1, 3, 5, 10, 7, 4, 9, 2, 8], 54) == 10

print("All tests passed!")
