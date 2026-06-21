# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/92335


def convert_to_base(n: int, k: int) -> str:
    digits = ""
    
    while n > 0:
        quotient = n // k
        remainder = n % k
        digits = str(remainder) + digits
        n = quotient
    
    return digits


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def solution(n: int, k: int) -> int:
    answer = 0
    digits = convert_to_base(n, k)

    candidates = digits.split("0")
    for candidate in candidates:
        if candidate != "" and is_prime(int(candidate)):
            answer += 1
    
    return answer


assert convert_to_base(10, 10) == "10"
assert convert_to_base(10, 2) == "1010"
assert convert_to_base(10, 3) == "101"

assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(4) == False

assert solution(437674, 3) == 3
assert solution(110011, 10) == 2

print("All tests passed!")