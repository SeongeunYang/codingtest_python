import sys
def intput(): return sys.stdin.readline().rstrip()


N = input()
cycle = 0
N = "0" + N if int(N) < 10 else N
new_num = N
while True:
    last_num = new_num[1]
    step1 = str(int(new_num[0]) + int(new_num[1]))
    new_num = last_num + step1[len(step1)-1]

    cycle += 1
    if N == new_num:
        print(cycle)
        break