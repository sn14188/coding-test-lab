from itertools import permutations

POSSIBLE_OPERATORS = ["+", "-", "*"]


def solution(expression):
    used_operators = []
    for operator in POSSIBLE_OPERATORS:
        if operator in expression:
            used_operators.append(operator)

    operands = []
    operators = []
    num = ""
    for ch in expression:
        if ch in used_operators:
            operands.append(int(num))
            operators.append(ch)
            num = ""
        else:
            num += ch
    operands.append(int(num))

    answer = 0
    priorites = permutations(used_operators)
    for priority in priorites:
        curr_operands = operands[:]
        curr_operators = operators[:]

        for operator in priority:
            evaluated_operands = []
            evaluated_operands.append(curr_operands.pop(0))
            remaining_operators = []

            while curr_operators:
                if operator == curr_operators[0]:
                    operand_1 = evaluated_operands.pop()
                    operand_2 = curr_operands.pop(0)
                    curr_operator = curr_operators.pop(0)

                    if curr_operator == "+":
                        result = operand_1 + operand_2
                    elif curr_operator == "-":
                        result = operand_1 - operand_2
                    elif curr_operator == "*":
                        result = operand_1 * operand_2

                    evaluated_operands.append(result)
                else:
                    evaluated_operands.append(curr_operands.pop(0))
                    remaining_operators.append(curr_operators.pop(0))

            curr_operands = evaluated_operands
            curr_operators = remaining_operators

        answer = max(answer, abs(curr_operands[0]))

    return answer


assert solution("100-200*300-500+20") == 60420
assert solution("50*6-3*2") == 300

print("All tests passed!")
