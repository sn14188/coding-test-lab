# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/72411
#
# 메뉴 리뉴얼
#
# 레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로
# 구성하려고 고민하고 있습니다. 기존에는 단품으로만 제공하던 메뉴를 조합해서
# 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다.
#
# 스카피는 이전 손님 주문 데이터에서 가장 자주 함께 주문된 단품메뉴 조합을
# 코스요리로 구성하기로 결정합니다. 조건은 다음과 같습니다:
# - 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
# - 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴
#   후보에 포함
#
# 제한사항
# - orders 배열 크기: 2 이상 20 이하
# - 각 주문 문자열: 2 이상 10 이하 길이, 대문자 알파벳만 사용, 중복 없음
# - course 배열 크기: 1 이상 10 이하
# - course의 원소: 2 이상 10 이하 자연수, 오름차순 정렬, 중복 없음
# - 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로
#   오름차순 정렬해서 return (각 문자열도 알파벳 오름차순 정렬)
# - 최다 주문 조합이 여러 개면 모두 포함


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
