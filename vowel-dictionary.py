# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/84512


def solution(word: str) -> int:
    vowels = ["A", "E", "I", "O", "U"]

    def dfs(curr, counter):
        if curr:
            counter += 1
            if curr == word:
                return counter, True

        if len(curr) == 5:
            return counter, False

        for vowel in vowels:
            counter, found = dfs(curr + vowel, counter)
            if found:
                return counter, True

        return counter, False

    answer, _ = dfs("", 0)
    return answer


assert solution("AAAAE") == 6
assert solution("AAAE") == 10
assert solution("I") == 1563
assert solution("EIO") == 1189

print("All tests passed!")
