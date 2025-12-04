def solution(
    enroll: list[str], referral: list[str], seller: list[str], amount: list[int]
) -> list[int]:
    earnings = dict()
    referrals = dict()

    for i in range(len(enroll)):
        member = enroll[i]
        parent = referral[i]
        referrals[member] = parent

        earnings[member] = 0

    for i in range(len(seller)):
        member = seller[i]
        sales = amount[i] * 100

        while member != "-" and sales > 0:
            commission = sales // 10
            profit = sales - commission

            earnings[member] += profit

            parent = referrals[member]

            member = parent
            sales = commission

    answer = []
    for member in enroll:
        answer.append(earnings[member])

    return answer


assert solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],
    [12, 4, 2, 5, 10],
) == [360, 958, 108, 0, 450, 18, 180, 1080]
assert solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["sam", "emily", "jaimie", "edward"],
    [2, 3, 5, 4],
) == [0, 110, 378, 180, 270, 450, 0, 0]

print("All tests passed!")
