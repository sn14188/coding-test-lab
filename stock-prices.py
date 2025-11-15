def solution(prices: list[int]) -> list[int]:
    answer = []

    for i in range(len(prices)):
        target = prices[i]

        duration = 0
        for j in range(i + 1, len(prices)):
            if target <= prices[j]:
                duration += 1

        answer.append(duration)

    return answer


assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]

print("All tests passed!")
