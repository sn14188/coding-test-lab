def solution(progresses: list[int], speeds: list[int]) -> list[int]:
    progresses_copy = progresses[:]
    speeds_copy = speeds[:]

    answer = []
    while progresses_copy:
        for i in range(len(progresses_copy)):
            if progresses_copy[i] >= 100:
                continue
            else:
                progresses_copy[i] += speeds_copy[i]

        head = progresses_copy[0]
        if head >= 100:
            counter = 0
            while progresses_copy and progresses_copy[0] >= 100:
                progresses_copy.pop(0)
                speeds_copy.pop(0)
                counter += 1

            answer.append(counter)

    return answer


assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]

print("All tests passed!")
