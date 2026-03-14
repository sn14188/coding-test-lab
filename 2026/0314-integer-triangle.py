# problem url: https://www.acmicpc.net/problem/1932


def max_triangle_path(triangle: list[list[int]]) -> int:
    for row_index in range(1, len(triangle)):
        prev_row = triangle[row_index - 1]
        curr_row = triangle[row_index]

        for i in range(len(curr_row)):
            if i == 0:
                curr_row[i] += prev_row[0]
            elif i == len(curr_row) - 1:
                curr_row[i] += prev_row[len(prev_row) - 1]
            else:
                curr_row[i] += max(prev_row[i - 1], prev_row[i])

    last_row = triangle[-1]
    max_path_sum = max(last_row)

    return max_path_sum


assert max_triangle_path([[5]]) == 5
assert (
    max_triangle_path(
        [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]],
    )
    == 30
)
assert (
    max_triangle_path(
        [
            [1],
            [2, 2],
            [3, 3, 3],
        ]
    )
    == 6
)

print("All tests passed!")
