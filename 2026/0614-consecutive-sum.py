# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/12924


def solution(n: int) -> int:
    answer = 0

    for i in range(1, n + 1):
        temp = 0
        for j in range(i, n + 1):
            temp += j
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break

    return answer


assert solution(15) == 4

print("All tests passed!")
