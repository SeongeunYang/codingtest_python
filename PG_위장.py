def solution(clothes):
    kinds = {}
    for i in clothes:
        if i[1] in kinds:
            kinds[i[1]] += 1
        else:
            kinds[i[1]] = 1

    cnt = 1
    for j in kinds.values():
        cnt = cnt * (j + 1)

    return cnt - 1


if __name__ == "__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    result = solution(clothes)
    print(result)
