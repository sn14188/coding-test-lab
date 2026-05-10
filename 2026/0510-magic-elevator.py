# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/148653


def solution(storey: int) -> int:
    answer = 0

    while storey > 0:
        current = storey % 10

        if current < 5:
            answer += current
        elif current > 5:
            answer += 10 - current
            storey += 10 - current
        else:
            upper = (storey // 10) % 10
            answer += 5
            if upper >= 5:
                storey += 5

        storey //= 10

    return answer


assert solution(16) == 6
assert solution(2554) == 16
assert solution(15) == 6
assert solution(95) == 6

print("All tests passed!")
