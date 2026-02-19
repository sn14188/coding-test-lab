# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42579


def solution(files: list[str]) -> list[str]:
    answer = []
    return answer


assert solution(
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
assert solution(
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
) == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

print("All tests passed!")
