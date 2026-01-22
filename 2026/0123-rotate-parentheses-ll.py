# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/76502


class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = None


def solution(s: str) -> int:
    head = Node(s[0])
    curr = head

    for c in s[1:]:
        curr.next = Node(c)
        curr = curr.next

    curr.next = head

    def is_right(start: Node) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        curr = start

        for _ in range(len(s)):
            p = curr.val
            curr = curr.next

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
    start = head

    for _ in range(len(s)):
        if is_right(start):
            answer += 1

        start = start.next

    return answer


assert solution("[](){}") == 3
assert solution("}]()[{") == 2
assert solution("[)(]") == 0
assert solution("}}}") == 0

print("All tests passed!")
