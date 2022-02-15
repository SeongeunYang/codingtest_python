def solution(numbers):
    prime_list = []
    chk_num = []

    for i in numbers:
        if int(i) not in chk_num:
            chk_num.append(int(i))
            if is_prime(int(i)):
                prime_list.append(int(i))
        sub_numbers = numbers.replace(i, '', 1)
        search_num(sub_numbers, i, chk_num, prime_list)

    count = len(prime_list)
    return count


def search_num(numbers, i, chk_num, prime_list):
    for j in numbers:
        num = i + j
        if int(num) not in chk_num:
            chk_num.append(int(num))
            if is_prime(int(num)):
                prime_list.append(int(num))
        sub_numbers = numbers.replace(j, '', 1)
        search_num(sub_numbers, num, chk_num, prime_list)


def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(solution("17"))
