import queue
import sys
input = lambda : sys.stdin.readline().rstrip()

n,m=map(int, input().split())
ary=[list(map(int,input())) for _ in range(n)]

flag = [[0]*m for _ in range(n)]
flag[0][0] = 1
dx=[-1,0,1,0]
dy=[0,1,0,-1]
q=queue.Queue()
q.put([0, 0])
flag[0][0]=1

while not q.empty():
    now_x, now_y = q.get()
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        if nx<0 or nx>=n: continue
        if ny<0  or ny>=m: continue
        if ary[nx][ny] == 0: continue
        if flag[nx][ny] != 0: continue
        q.put([nx,ny])
        flag[nx][ny] = flag[now_x][now_y] + 1

print(flag[n-1][m-1])