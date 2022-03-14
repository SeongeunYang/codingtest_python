from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    comb = list(combinations(s,6))

    for x in comb:
        print(*x)
    print()