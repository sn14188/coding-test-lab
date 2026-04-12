# problem url: https://www.codetree.ai/ko/frequent-problems/all/problems/security-manager/description


def solution(sequence: str) -> bool:
    return False


assert solution("(?(??)") == True
assert solution("(((())") == False
assert solution("?????") == False

print("All tests passed!")
