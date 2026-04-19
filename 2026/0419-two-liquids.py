# problem url: https://www.acmicpc.net/problem/2470


def solution(liquids: list[int]) -> list[int]:
    liquids.sort()

    left_idx, right_idx = 0, len(liquids) - 1
    best = float("inf")
    answer = []

    while left_idx < right_idx:
        mixed = liquids[left_idx] + liquids[right_idx]

        if abs(mixed) < best:
            best = abs(mixed)
            answer = [liquids[left_idx], liquids[right_idx]]

        if mixed < 0:
            left_idx += 1
        else:
            right_idx -= 1

    return answer


# # brute force
# def solution(liquids: list[int]) -> list[int]:
#     best = float("inf")
#     answer = []

#     for i in range(len(liquids)):
#         for j in range(i + 1, len(liquids)):
#             mixed = liquids[i] + liquids[j]

#             if abs(mixed) < best:
#                 best = abs(mixed)
#                 answer = sorted([liquids[i], liquids[j]])

#     return answer


assert solution([-2, 4, -99, -1, 98]) == [-99, 98]
assert solution([-100, -2, 4, 103]) == [-2, 4]

print("All tests passed!")
