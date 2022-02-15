def solution(genres, plays):
    album = {}
    sum_plays = {}
    for i in range(0, len(genres)):
        if genres[i] in album:
            album[genres[i]].append((plays[i], i))
            sum_plays[genres[i]] += plays[i]
        else:
            album[genres[i]] = [(plays[i], i)]
            sum_plays[genres[i]] = plays[i]

    sum_plays = sorted(sum_plays.items(), key=lambda x: x[1], reverse=True)
    answer = []
    for g in sum_plays:
        slist = sorted(album[g[0]], reverse=True)
        # for i in range(0, ):

    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    results = solution(genres, plays)
    print(results)
