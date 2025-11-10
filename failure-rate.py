def solution(N: int, stages: list[int]) -> list[int]:
    failure_rates = {}
    remaining_players = len(stages)

    for stage in range(1, N + 1):
        if stage in stages:
            failed_players = stages.count(stage)
            failure_rate = failed_players / remaining_players
            remaining_players -= failed_players
            failure_rates[stage] = failure_rate
        else:
            failure_rates[stage] = 0

    answer = sorted(failure_rates.keys(), key=lambda x: failure_rates[x], reverse=True)

    return answer


assert solution(5, [2, 1, 2, 6, 2, 4, 3, 3]) == [3, 4, 2, 1, 5]
assert solution(4, [4, 4, 4, 4, 4]) == [4, 1, 2, 3]

print("All tests passed!")
