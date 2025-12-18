# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/43162


class Queue:
    def __init__(self):
        self.items = []
        self.front = 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        elem = self.items[self.front]
        self.front += 1
        return elem

    def is_empty(self):
        return self.front >= len(self.items)


def solution(n: int, computers: list[list[int]]) -> int:
    visited = [False] * n

    def bfs(start_node):
        queue = Queue()
        queue.push(start_node)
        visited[start_node] = True

        while not queue.is_empty():
            curr = queue.pop()

            for i in range(n):
                if computers[curr][i] == 1 and visited[i] == False:
                    queue.push(i)
                    visited[i] = True

    answer = 0
    for i in range(n):
        if visited[i] == False:
            answer += 1
            bfs(i)

    return answer


assert solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
assert solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]) == 1

print("All tests passed!")
