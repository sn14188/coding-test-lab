# problem url: https://school.programmers.co.kr/learn/courses/30/lessons/42579


def solution(genres: list[str], plays: list[int]) -> list[int]:
    total_play = dict()
    for i in range(len(genres)):
        genre = genres[i]

        if genre in total_play:
            total_play[genre] += plays[i]
        else:
            total_play[genre] = plays[i]

    genre_unique = set(genres)

    genre_order = sorted(genre_unique, key=lambda x: total_play[x], reverse=True)
    genre_order = [genre for genre in genre_order if total_play[genre] > 0]

    answer = []
    for genre in genre_order:
        songs = []

        for i in range(len(genres)):
            if genres[i] == genre:
                songs.append((i, plays[i]))

        songs.sort(key=lambda x: (-x[1], x[0]))

        answer.append(songs[0][0])
        if len(songs) > 1:
            answer.append(songs[1][0])

    return answer


assert solution(
    ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
) == [4, 1, 3, 0]
assert solution(["classic", "pop"], [500, 400]) == [0, 1]
assert solution(
    ["classic", "pop", "classic", "kpop", "kpop"], [500, 600, 150, 1000, 1000]
) == [3, 4, 0, 2, 1]

print("All tests passed!")
