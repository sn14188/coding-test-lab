# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42579


def solution(files: list[str]) -> list[str]:
    def split_file_name(file_name: str) -> tuple[str, str]:
        index = 0
        head_part = ""

        while index < len(file_name) and not file_name[index].isdigit():
            head_part += file_name[index]
            index += 1

        number_part = ""
        while index < len(file_name) and file_name[index].isdigit():
            number_part += file_name[index]
            index += 1

        return head_part, number_part

    parsed_files = []

    for file_name in files:
        head_part, number_part = split_file_name(file_name)
        parsed_files.append((head_part.lower(), int(number_part), file_name))

    parsed_files.sort(key=lambda item: (item[0], item[1]))

    answer = []
    for item in parsed_files:
        answer.append(item[2])

    return answer


assert solution(
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
assert solution(
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
) == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

print("All tests passed!")
