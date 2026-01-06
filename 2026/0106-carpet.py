# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown: int, yellow: int) -> list[int]:
    total_tiles = brown + yellow
    candidates = []

    yellow_height = 1
    while yellow >= yellow_height:
        if yellow % yellow_height == 0:
            yellow_width = yellow // yellow_height
            candidates.append([yellow_width, yellow_height])

        yellow_height += 1

    answer = []
    for yellow_width, yellow_height in candidates:
        carpet_width = yellow_width + 2
        carpet_height = yellow_height + 2

        if carpet_width * carpet_height == total_tiles:
            answer += [carpet_width, carpet_height]
            break

    return answer


assert solution(10, 2) == [4, 3]
assert solution(8, 1) == [3, 3]
assert solution(24, 24) == [8, 6]

print("All tests passed!")
