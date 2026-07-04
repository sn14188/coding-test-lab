# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/468370


def overlaps_any_spoiler(word_start, word_end, spoiler_ranges):
    for spoiler_start, spoiler_end in spoiler_ranges:
        if word_start <= spoiler_end and spoiler_start <= word_end:
            return True

    return False


def solution(message: str, spoiler_ranges: list[list[int]]) -> int:
    answer = 0

    words = []
    tokens = message.split(" ")

    current_index = 0
    for token in tokens:
        word_start = current_index
        word_end = current_index + len(token) - 1
        words.append((token, word_start, word_end))
        current_index = word_end + 2

    clean_word_values = set()
    for word_value, word_start, word_end in words:
        if not overlaps_any_spoiler(word_start, word_end, spoiler_ranges):
            clean_word_values.add(word_value)

    counted_word_values = set()
    for word_value, word_start, word_end in words:
        if word_value in clean_word_values or word_value in counted_word_values:
            continue
        if overlaps_any_spoiler(word_start, word_end, spoiler_ranges):
            answer += 1
            counted_word_values.add(word_value)

    return answer


assert solution("here is muzi here is a secret message", [[0, 3], [23, 28]]) == 1
assert (
    solution(
        "my phone number is 01012345678 and may i have your phone number",
        [[5, 5], [25, 28], [34, 40], [53, 59]],
    )
    == 4
)

print("All tests passed!")
