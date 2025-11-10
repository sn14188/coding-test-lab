def solution(arr1, arr2):
    """
    example:
    arr1   arr2   return
    1 4    3 3    15 15
    3 2    3 3    15 15
    4 1           15 15
    """
    arr2_cols = []
    for i in range(len(arr2[0])):
        col = []
        for j in range(len(arr2)):
            col.append(arr2[j][i])

        arr2_cols.append(col)

    answer = []
    for row in arr1:
        answer_row = []
        for col in arr2_cols:
            val = 0
            for a, b in zip(row, col):
                val += a * b

            answer_row.append(val)
        answer.append(answer_row)

    return answer


assert solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) == [
    [15, 15],
    [15, 15],
    [15, 15],
]
assert solution(
    [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
) == [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

print("All tests passed!")
