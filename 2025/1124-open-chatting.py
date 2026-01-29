def solution(record: list[str]) -> list[str]:
    accounts = dict()
    for r in record:
        elems = r.split()
        if len(elems) == 3:
            id, name = elems[1], elems[2]
            accounts[id] = name

    answer = []
    for r in record:
        elems = r.split()
        event, id = elems[0], elems[1]
        name = accounts[id]

        if event == "Enter":
            message_event = "님이 들어왔습니다."
        elif event == "Leave":
            message_event = "님이 나갔습니다."
        else:
            continue

        message = name + message_event
        answer.append(message)

    return answer


assert solution(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
) == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

assert solution(
    [
        "Enter uid4567 Prodo",
        "Change uid4567 Ryan",
        "Change uid4567 Muzi",
        "Change uid4567 Aiden",
    ]
) == ["Aiden님이 들어왔습니다."]

print("All tests passed!")
