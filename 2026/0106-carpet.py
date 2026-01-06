# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown: int, yellow: int) -> list[int]:
    total_tiles = brown + yellow

    answer = []
    for yellow_width in range(yellow, 0, -1):
        if yellow % yellow_width == 0:
            yellow_height = yellow // yellow_width

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
