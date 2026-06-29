# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/468370


def solution(message: str, spoiler_ranges: list[list[int]]) -> int:
    answer = 0
    return answer


assert solution("here is muzi here is a secret message", [[0, 3], [23, 28]]) == 1
assert (
    solution(
        "my phone number is 01012345678 and may i have your phone number",
        [[5, 5], [25, 28], [34, 40], [53, 59]],
    )
    == 4
)

print("All tests passed!")
