# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42583


def solution(bridge_length: int, weight: int, truck_weights: list[int]) -> int:
    duration = 0
    bridge = [0] * bridge_length
    bridge_weight = 0

    while truck_weights or bridge_weight > 0:
        duration += 1

        bridge_out = bridge.pop(0)
        bridge_weight -= bridge_out

        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            truck_weight = truck_weights.pop(0)
            bridge.append(truck_weight)
            bridge_weight += truck_weight
        else:
            bridge.append(0)

    return duration


assert solution(2, 10, [7, 4, 5, 6]) == 8
assert solution(100, 100, [10]) == 101
assert solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110

print("All tests passed!")
