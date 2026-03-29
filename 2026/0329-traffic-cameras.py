# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes: list[list[int]]) -> int:
    routes.sort(key=lambda x: x[1])

    answer = 0
    last_camera = float("-inf")

    for start, end in routes:
        if start > last_camera:
            answer += 1
            last_camera = end

    return answer


assert solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]) == 2

print("All tests passed!")
