# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/154539


def solution(numbers: list[int]) -> list[int]:
    n = len(numbers)
    answer = [-1] * n
    stack = []

    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]

        stack.append(i)

    return answer


# # brute force
# def solution(numbers: list[int]) -> list[int]:
#     answer = []

#     for i in range(len(numbers)):
#         found = -1

#         for j in range(i + 1, len(numbers)):
#             if numbers[i] < numbers[j]:
#                 found = numbers[j]
#                 break

#         answer.append(found)

#     return answer


assert solution([2, 3, 3, 5]) == [3, 5, 5, -1]
assert solution([9, 1, 5, 3, 6, 2]) == [-1, 5, 6, 6, -1, -1]

print("All tests passed!")
