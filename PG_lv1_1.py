def solution(n, m):
    answer = [n, m]
    max = n
    min = m
    if m == n:
        return answer
    elif m > n:
        max = m
        min = n

    while min != 0:
        remainder = max % min
        max = min
        min = remainder

    answer[0] = max
    answer[1] = max * (n / max) * (m / max)

    return answer


if __name__ == "__main__":
    print(solution(3, 12))
