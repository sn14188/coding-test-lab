# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/43163


def solution(begin: str, target: str, words: list[str]) -> int:
    visited = [False] * len(words)

    def is_one_letter_diff(word_1: str, word_2: str) -> bool:
        num_diff = 0

        for i in range(len(word_1)):
            if word_1[i] != word_2[i]:
                num_diff += 1

        return num_diff == 1

    def dfs(curr: str, depth: int) -> int:
        if curr == target:
            return depth

        min_depth = float("inf")

        for i in range(len(words)):
            word = words[i]
            if is_one_letter_diff(curr, word) and visited[i] == False:
                visited[i] = True
                candidate = dfs(word, depth + 1)
                visited[i] = False

                min_depth = min(min_depth, candidate)

        return min_depth

    answer = dfs(begin, 0)
    if answer == float("inf"):
        return 0

    return answer


assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0

print("All tests passed!")
