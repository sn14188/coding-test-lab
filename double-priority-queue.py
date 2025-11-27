import time


def solution(operations: list[str]) -> list[int]:
    answer = []

    for operation in operations:
        elems = operation.split()
        command, num = elems[0], int(elems[1])

        if command == "I":
            answer.append(num)
        elif command == "D":
            if not answer:
                pass
            elif num == 1:
                max_num = max(answer)
                answer.remove(max_num)
            elif num == -1:
                min_num = min(answer)
                answer.remove(min_num)

    if not answer:
        return [0, 0]

    return [max(answer), min(answer)]


start = time.time()
assert solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]) == [0, 0]
assert solution(
    ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
) == [333, -45]
assert solution(
    [
        "I 5",
        "I 3",
        "I 9",
        "D 1",
        "I -7",
        "I 10",
        "I 10",
        "D -1",
        "I 8",
        "I -2",
        "D 1",
        "I 100",
        "I -100",
        "I 50",
        "D -1",
        "I 7",
        "I 6",
        "I -3",
        "D 1",
        "D -1",
        "I 42",
        "I 99",
        "I -42",
        "I 0",
        "D 1",
        "D -1",
        "I 13",
        "I -57",
        "I 88",
        "I 88",
        "D 1",
        "I -999",
        "I 777",
        "I 555",
        "D -1",
        "I 444",
        "I 333",
        "I 222",
        "D 1",
        "I -111",
        "I 11",
        "I 22",
        "I 33",
        "I 44",
        "D -1",
        "I 123",
        "I 321",
        "I -321",
        "I 999",
        "D 1",
        "I -5",
        "I -6",
        "I -7",
        "D -1",
        "D 1",
        "I 314",
        "I 159",
        "I 265",
        "I 358",
        "I 979",
        "D -1",
        "D 1",
        "I -1000",
        "I 1000",
        "I -500",
        "I 500",
        "D 1",
        "D -1",
        "I 17",
        "I 27",
        "I 37",
        "I 47",
        "I 57",
        "D 1",
        "I -17",
        "I -27",
        "I -37",
        "I -47",
        "I -57",
        "D -1",
        "I 101",
        "I 202",
        "I 303",
        "I 404",
        "I 505",
        "D -1",
        "D 1",
        "I -808",
        "I 909",
        "I -909",
        "D 1",
        "D -1",
        "I 12",
        "I 24",
        "I 36",
        "I 48",
        "I 60",
        "D 1",
        "I -12",
        "I -24",
        "I -36",
        "I -48",
        "D -1",
        "I 100",
        "I 200",
        "I 300",
        "I 400",
        "I 500",
        "D -1",
        "I -100",
        "I -200",
        "I -300",
        "I -400",
        "I -500",
        "D 1",
        "I 73",
        "I 74",
        "I 75",
        "I 76",
        "I 77",
        "D -1",
        "I -73",
        "I -74",
        "I -75",
        "I -76",
        "I -77",
        "D 1",
    ]
) == [400, -400]
end = time.time()

print("************")
print("All tests passed!")
print(f"Duration: {end - start:.6f} seconds")  # 0.000088 seconds
print("************")
