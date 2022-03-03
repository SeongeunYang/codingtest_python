import sys
def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
flag = [False, False] + [True]*(M-1)
for i in range(2, M + 1):
    if flag[i]:
        if i >= N and i <= M:
            print(i)
        for j in range(2*i, M + 1, i):
            flag[j] = False