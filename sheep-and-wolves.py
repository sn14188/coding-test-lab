def solution(info: list[int], edges: list[list[int]]) -> int:
    tree = {}
    for edge in edges:
        key, val = edge[0], edge[1]

        if key not in tree:
            tree[key] = [val]
        else:
            tree[key].append(val)

    def dfs(curr, candidates, sheep, wolves):
        if info[curr] == 0:
            sheep += 1
        else:
            wolves += 1

        if wolves >= sheep:
            return 0

        max_sheep = sheep

        candidates_copy = candidates.copy()
        candidates_copy.remove(curr)

        if curr in tree:
            for child in tree[curr]:
                candidates_copy.append(child)

        for candidate in candidates_copy:
            max_sheep = max(max_sheep, dfs(candidate, candidates_copy, sheep, wolves))

        return max_sheep

    answer = dfs(0, [0], 0, 0)

    return answer


assert (
    solution(
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [
            [0, 1],
            [1, 2],
            [1, 4],
            [0, 8],
            [8, 7],
            [9, 10],
            [9, 11],
            [4, 3],
            [6, 5],
            [4, 6],
            [8, 9],
        ],
    )
    == 5
)
assert (
    solution(
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [
            [0, 1],
            [0, 2],
            [1, 3],
            [1, 4],
            [2, 5],
            [2, 6],
            [3, 7],
            [4, 8],
            [6, 9],
            [9, 10],
        ],
    )
    == 5
)

print("All tests passed!")
