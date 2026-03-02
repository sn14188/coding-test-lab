# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42895


def solution(N: int, number: int) -> int:
    def combine(set_1: set[int], set_2: set[int]) -> set[int]:
        result = set()

        for a in set_1:
            for b in set_2:
                result.add(a + b)
                result.add(a - b)
                result.add(a * b)

                if b != 0:
                    result.add(a // b)

        return result

    if N == number:
        return 1

    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(2, 9):
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            dp[i] = dp[i] | combine(dp[j], dp[i - j])

            if number in dp[i]:
                return i

    return -1


assert solution(5, 12) == 4
assert solution(2, 11) == 3

print("All tests passed!")
