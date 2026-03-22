# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42861


def solution(n: int, costs: list[list[int]]) -> int:
    parents = [i for i in range(n)]

    def find(x: int) -> int:
        if parents[x] != x:
            return find(parents[x])

        return parents[x]

    def union(a: int, b: int) -> None:
        parent_1 = find(a)
        parent_2 = find(b)

        if parent_1 != parent_2:
            parents[parent_2] = parent_1

    costs.sort(key=lambda x: x[2])

    answer = 0
    for a, b, cost in costs:
        if find(a) != find(b):
            union(a, b)
            answer += cost

    return answer


assert solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]) == 4

print("All tests passed!")
