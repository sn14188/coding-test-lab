# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil


def solution(fees: list[int], records: list[str]) -> list[int]:
    """
    idea:
    - records -> records_dict: 시간을 기록해야겠다고 생각, 타임스탬프도 같이 기록해야 함, 상태도 알아야 함
    - IN: 타임스탬프 기록
    - OUT: 체류 시간 계산 & 기록
    - 이후 요금 계산
    """
    records_dict = dict()

    for record in records:
        time_stamp, plate, status = record.split()
        """
        분 단위로 기록 -> 계산하기 편하고 저장부터 그렇게 해놓으면 사용하기 쉬움
        """
        hour, minute = time_stamp.split(":")
        hour_int = int(hour)
        minute_int = int(minute)
        ts_as_minute = hour_int * 60 + minute_int

        if status == "IN":
            if plate not in records_dict:
                records_dict[plate] = {"in": ts_as_minute, "total": 0}
            else:
                records_dict[plate]["in"] = ts_as_minute
        else:
            stay = ts_as_minute - records_dict[plate]["in"]
            records_dict[plate]["total"] += stay
            records_dict[plate]["in"] = None

    for plate, info in records_dict.items():
        if info["in"] is not None:
            stay = 23 * 60 + 59 - info["in"]
            info["total"] += stay

    answer = []
    base_time, base_fee, unit_time, unit_fee = fees
    sorted_plates = sorted(records_dict)

    for plate in sorted_plates:
        total = records_dict[plate]["total"]

        if total <= base_time:
            answer.append(base_fee)
        else:
            fee = base_fee + ceil((total - base_time) / unit_time) * unit_fee
            answer.append(fee)

    return answer


assert solution(
    [180, 5000, 10, 600],
    [
        "05:34 5961 IN",
        "06:00 0000 IN",
        "06:34 0000 OUT",
        "07:59 5961 OUT",
        "07:59 0148 IN",
        "18:59 0000 IN",
        "19:09 0148 OUT",
        "22:59 5961 IN",
        "23:00 5961 OUT",
    ],
) == [14600, 34400, 5000]
assert solution(
    [120, 0, 60, 591],
    [
        "16:00 3961 IN",
        "16:00 0202 IN",
        "18:00 3961 OUT",
        "18:00 0202 OUT",
        "23:58 3961 IN",
    ],
) == [0, 591]
assert solution([1, 461, 1, 10], ["00:00 1234 IN"]) == [14841]

print("All tests passed!")
