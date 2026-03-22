# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(people: list[int], limit: int) -> int:
    people.sort()

    left = 0
    right = len(people) - 1

    answer = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1

        answer += 1
        right -= 1

    return answer


assert solution([70, 50, 80, 50], 100) == 3
assert solution([70, 80, 50], 100) == 3

assert solution([40, 50], 100) == 1
assert solution([50, 50], 100) == 1
assert solution([50, 51], 100) == 2

print("All tests passed!")
