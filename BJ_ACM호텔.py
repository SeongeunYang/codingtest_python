import sys
def input(): return sys.stdin.readline().rstrip()


T = int(input())

guest = [list(map(int, input().split())) for _ in range(T)]

for H, W, N in guest:
    if N % H == 0:
        floor = H
        num = N//H -1
    else:
        num = N//H
        floor = N % H
    print( floor * 100 + num + 1)