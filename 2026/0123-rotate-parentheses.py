# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/76502


def solution(s: str) -> int:
    candidates = []
    for i in range(len(s)):
        candidate = s[i:] + s[:i]
        candidates.append(candidate)

    def is_right(parens: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for p in parens:
            if p in "([{":
                stack.append(p)
            else:
                if not stack:
                    return False

                the_last = stack.pop()
                if the_last != pairs[p]:
                    return False

        return not stack

    answer = 0
    for candidate in candidates:
        if is_right(candidate):
            answer += 1

    return answer


assert solution("[](){}") == 3
assert solution("}]()[{") == 2
assert solution("[)(]") == 0
assert solution("}}}") == 0

print("All tests passed!")
