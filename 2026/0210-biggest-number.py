# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42746

from itertools import permutations


def solution(numbers: list[int]) -> str:
    answer = ""
    return answer


# selection sort
def solution_ss(numbers: list[int]) -> str:
    str_numbers = list(map(str, numbers))

    for i in range(len(str_numbers)):
        best = i
        for j in range(i + 1, len(str_numbers)):
            if str_numbers[best] + str_numbers[j] < str_numbers[j] + str_numbers[best]:
                best = j

        str_numbers[i], str_numbers[best] = str_numbers[best], str_numbers[i]

    answer = "".join(str_numbers)

    return answer


# brute force
def solution_bf(numbers: list[int]) -> str:
    biggest_num = 0

    for permutation in permutations(numbers):
        num = int("".join(map(str, permutation)))
        biggest_num = max(num, biggest_num)

    answer = str(biggest_num)

    return answer


assert solution([6, 10, 2]) == "6210"
assert solution([3, 30, 34, 5, 9]) == "9534330"

print("All tests passed!")
