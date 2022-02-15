def solution(numbers, target):
    result = 0

    def dfs(num, level):
        nonlocal result
        if level == len(numbers):
            if num == target:
                result += 1
            return

        signs = [-num, num]
        if level == 1:
            for sign in signs:
                dfs(sign + numbers[level], level + 1)
                dfs(sign - numbers[level], level + 1)
        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)

    dfs(numbers[0], 1)

    return result


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
