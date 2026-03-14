# problem url: https://www.acmicpc.net/problem/1932


def max_triangle_path(triangle: list[list[int]]) -> int:
    return -1


assert (
    max_triangle_path(
        [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]],
    )
    == 30
)

print("All tests passed!")
