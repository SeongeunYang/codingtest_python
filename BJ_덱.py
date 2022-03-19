from collections import deque
import sys
input=lambda : sys.stdin.readline().rstrip()

dq = deque()
N=int(input())
for i in range(N):
    comd, *X = input().split()
    if comd =="push_front":
        dq.appendleft(int(X[0]))
    elif comd =="push_back":
        dq.append(int(X[0]))
    elif comd =="pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif comd =="pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif comd == "size":
        print(len(dq))
    elif comd == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif comd == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif comd == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])