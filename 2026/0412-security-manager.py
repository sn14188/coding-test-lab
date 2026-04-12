# problem url: https://www.codetree.ai/ko/frequent-problems/all/problems/security-manager/description


def solution(sequence: str) -> bool:
    if len(sequence) % 2 == 1:
        return False

    max_in, min_in = 0, 0

    for s in sequence:
        if s == "(":
            max_in += 1
            min_in += 1
        elif s == ")":
            max_in -= 1
            min_in -= 1
        else:
            max_in += 1
            min_in -= 1

        if max_in < 0:
            return False

        if min_in < 0:
            min_in = 0

        # print("")
        # print(f"max_in: {max_in}")
        # print(f"min_in: {min_in}")

    return min_in == 0


assert solution("(?(??)") == True
assert solution("(((())") == False
assert solution("?????") == False

# added cases
assert solution("()") == True
assert solution("((") == False
assert solution("))") == False
assert solution("(()())") == True

assert solution("??") == True
assert solution("???") == False

print("All tests passed!")
