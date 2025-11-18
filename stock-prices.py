def solution(prices: list[int]) -> list[int]:
    answer = [0] * len(prices)
    stack = []

    for idx, price in enumerate(prices):
        if idx == 0:
            stack.append(0)
            continue

        top = prices[stack[-1]]
        if top <= price:
            stack.append(idx)
        else:
            while prices[stack[-1]] > price:
                top_idx = stack.pop()
                duration = idx - top_idx
                answer[top_idx] = duration
            stack.append(idx)

    last_idx = len(prices) - 1
    while stack:
        idx = stack.pop()
        answer[idx] = last_idx - idx

    return answer


assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]
assert solution([1, 2, 7, 10, 12, 4, 2]) == [6, 5, 3, 2, 1, 1, 0]

print("All tests passed!")
