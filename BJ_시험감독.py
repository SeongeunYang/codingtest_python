import sys
import math
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

s=N
for j in range(N):
    if A[j]- B > 0:
        sn = math.ceil((A[j]-B) / C)
        s += sn
print(s)