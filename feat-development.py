from collections import deque
import math
import time


def solution(progresses: list[int], speeds: list[int]) -> list[int]:
    q = deque()
    for i in range(len(progresses)):
        day_left = math.ceil((100 - progresses[i]) / speeds[i])
        q.append(day_left)

    answer = []
    front = q[0]
    counter = 0
    while q:
        if front >= q[0]:
            q.popleft()
            counter += 1
        else:
            answer.append(counter)
            counter = 0
            front = q[0]

    answer.append(counter)

    return answer


start = time.time()
assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]
end = time.time()

print("************")
print("All tests passed!")
print(f"Duration: {end - start:.6f} seconds")
print("************")
