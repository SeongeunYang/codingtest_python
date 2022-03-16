import queue
import sys
input = lambda : sys.stdin.readline().rstrip()

q = queue.Queue()
N = int(input())
for i in range(N):
    command, *x = input().split()
    if command == "push":
        q.put(int(x[0]))
    elif command == "pop":
        if not q.empty():
            print(q.get())
        else:
            print(-1)
    elif command == "size":
        print(q.qsize())
    elif command == "empty":
        if q.empty():
            print(1)
        else:
            print(0)
    elif command == "front":
        if not q.empty():
            print(q.queue[0])
        else:
            print(-1)
    elif command == "back":
        if not q.empty():
            print(q.queue[-1])
        else:
            print(-1)
    else:
        print("Wrong Command!!")
        i=i-1