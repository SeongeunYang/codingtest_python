import sys
def input(): return sys.stdin.readline().rstrip()


A, B, V = map(int, input().split())

if(A>=V):
    result = 1
else:
    result = (V-A)//(A-B)+1 if(V-A)%(A-B) == 0 else (V-A)//(A-B)+2
print(result)