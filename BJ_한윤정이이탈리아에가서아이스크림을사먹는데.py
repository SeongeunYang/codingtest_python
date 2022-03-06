from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()

n, m = map(int, input().split())
x=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    c1,c2 = list(map(int, input().split()))
    x[c1][c2] = 1
    x[c2][c1] = 1
result = list(combinations(range(1,n+1),3))

count=0
for r in result:
    if x[r[0]][r[1]] or x[r[1]][r[2]] or x[r[0]][r[2]]:
        continue
    count += 1
print(count)