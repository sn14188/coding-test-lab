def solution(s: str) -> str:
    nums_str = s.split(" ")

    nums = []
    for num_str in nums_str:
        nums.append(int(num_str))

    return f"{min(nums)} {max(nums)}"


assert solution("1 2 3 4") == "1 4"
assert solution("-1 -2 -3 -4") == "-4 -1"
assert solution("-1 -1") == "-1 -1"

print("All tests passed!")
