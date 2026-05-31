# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/12951


def solution(s: str) -> str:
    """
    idea:
    - 플래그를 만들어서 새 단어의 시작 여부를 확인
    - 루프를 돌며 업데이트
    """
    answer = ""

    is_word_started = True
    for c in s:
        if c == " ":
            is_word_started = True
            answer += c
        else:
            if is_word_started:
                answer += c.upper()
                is_word_started = False
            else:
                answer += c.lower()

    return answer


assert solution("3people unFollowed me") == "3people Unfollowed Me"
assert solution("for the last week") == "For The Last Week"
assert solution("test  test") == "Test  Test"

print("All tests passed!")
