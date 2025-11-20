import math


def solution(progresses: list[int], speeds: list[int]) -> list[int]:
    days_left = []
    for i in range(len(progresses)):
        day_left = math.ceil((100 - progresses[i]) / speeds[i])
        days_left.append(day_left)

    answer = []
    front = days_left[0]
    counter = 0
    while days_left:
        if front >= days_left[0]:
            days_left.pop(0)
            counter += 1
        else:
            answer.append(counter)
            counter = 0
            front = days_left[0]

    answer.append(counter)

    return answer


assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]

print("All tests passed!")
