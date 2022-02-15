def solution(brown, yellow):
    answer = []
    if yellow == 1:
        answer = [3, 3]

    for i in range(1, yellow):  # 노란 색의 세로길이
        if yellow % i != 0:
            continue

        width = yellow // i
        if (2 * i + 2 * (width + 2)) == brown:
            answer = [width + 2, i + 2]
            break

    return answer


if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(24, 24))
