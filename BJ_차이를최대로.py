from itertools import permutations
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
p = list(map(int, input().split()))
comb = list(permutations(p))

res=0
for l in comb:
    sum=0
    for i in range(n-1):
        sum+=abs(l[i]-l[i+1])
    res = max(res, sum)
print(res)