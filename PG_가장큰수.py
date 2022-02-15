def solution(numbers):
    if numbers.count(0) == len(numbers):
        return "0"

    str_numbers = list(map(lambda x: str(x) * 3, numbers))
    str_numbers.sort(reverse=True)
    result = list(map(lambda x: x[:len(x) // 3], str_numbers))

    answer = ''
    for num in result:
        answer = answer + num

    return answer


if __name__ == "__main__":
    numbers = [0, 0, 0, 0]
    print(solution(numbers))
