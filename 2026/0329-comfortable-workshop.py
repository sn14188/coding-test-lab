# problem url: https://www.codetree.ai/ko/frequent-problems/hsat/problems/easy-workshop/description


def solution(N: int, K: int, grid: list[list[int]]) -> int:
    dp = [[-1] * N for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    answer = float("inf")

    def dfs(x: int, y: int, length_so_far: int, max_diff: int) -> int:
        nonlocal answer

        if length_so_far >= K:
            answer = min(answer, max_diff)

        # 계산돼있고 현재 max_diff보다 작으면 재사용
        if dp[x][y] != -1 and dp[x][y] <= max_diff:
            return dp[x][y]

        local_min = float("inf")
        moved = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < N and 0 <= ny < N and grid[nx][ny] > grid[x][y]
            ):  # 그리드 안에 있고 오르막길이라면
                moved = True
                diff = grid[nx][ny] - grid[x][y]
                val = dfs(nx, ny, length_so_far + 1, max(max_diff, diff))
                local_min = min(local_min, val)

        if not moved:
            local_min = max_diff

        dp[x][y] = local_min

        return local_min

    for i in range(N):
        for j in range(N):
            dfs(i, j, 1, 0)

    return answer


assert solution(4, 3, [[6, 7, 8, 1], [9, 1, 1, 1], [1, 1, 4, 8], [1, 1, 1, 9]]) == 1
assert (
    solution(
        5,
        4,
        [
            [16, 57, 98, 11, 52],
            [49, 61, 71, 31, 39],
            [51, 41, 54, 88, 93],
            [71, 21, 31, 41, 20],
            [48, 34, 22, 50, 44],
        ],
    )
    == 10
)

print("All tests passed!")
