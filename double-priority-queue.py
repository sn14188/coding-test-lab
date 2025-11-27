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
end = time.time()

print("************")
print("All tests passed!")
print(f"Duration: {end - start:.6f} seconds")  # 0.000019 seconds
print("************")
