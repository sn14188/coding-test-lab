# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/12924


def solution(n: int) -> int:
    answer = 0

    for i in range(1, n + 1):
        running_sum = 0
        for j in range(i, n + 1):
            running_sum += j
            if running_sum == n:
                answer += 1
                break
            elif running_sum > n:
                break

    return answer


assert solution(15) == 4

print("All tests passed!")
