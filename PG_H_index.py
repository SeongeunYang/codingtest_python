def solution(citations):
    citations.sort()
    h = 0
    n = len(citations)
    for i in range(0, citations[n - 1]):
        for j in range(0, len(citations)):
            if citations[j] >= i:
                if len(citations[j:]) >= i:
                    h = i
                else:
                    break

    return h


if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))
