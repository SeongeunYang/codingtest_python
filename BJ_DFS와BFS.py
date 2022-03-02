import queue
import sys
input = lambda : sys.stdin.readline().rstrip()

n,m,s = map(int, input().split())
cent = [list() for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    cent[x].append(y)
    cent[y].append(x)

for i in cent:
    i.sort()

flag = [False] * (n+1)

def bfs(start):
    q = queue.Queue()
    q.put(start)
    flag[start] = True

    while not q.empty():
        now = q.get()
        print(now, end=" ")
        for next in cent[now]:
            if not flag[next]:
                flag[next] = True
                q.put(next)
    print()

def dfs(node):
    flag[node] = True
    print(node , end=" ")
    for next in cent[node]:
        if not flag[next]:
            dfs(next)

dfs(s)
print()
flag = [False]*(n+1)
bfs(s)