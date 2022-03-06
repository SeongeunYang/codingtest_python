import sys


def input(): return sys.stdin.readline().rstrip()


Nkg = int(input())
result = 0
while True:
    if Nkg < 5 and Nkg != 3:
        result = -1
        break
    elif Nkg % 5 == 0:
        result += (Nkg // 5)
        break
    else:
        result += 1
        Nkg -= 3
        if Nkg == 0:
            break

print(result)
