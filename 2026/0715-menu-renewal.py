# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/72411


def solution(orders: list[str], course: list[int]) -> list[str]:
    answer = []

    return answer


assert solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]) == [
    "AC",
    "ACDE",
    "BCFG",
    "CDE",
]
assert solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]) == [
    "ACD",
    "AD",
    "ADE",
    "CD",
    "XYZ",
]
assert solution(["XYZ", "XWY", "WXA"], [2, 3, 4]) == ["WX", "XY"]

print("All tests passed!")
