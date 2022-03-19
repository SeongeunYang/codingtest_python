from itertools import permutations
N=int(input())
result = list(permutations(range(1,N+1)))
for i in result:
    print(*i)