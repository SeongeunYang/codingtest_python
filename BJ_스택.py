import sys
input = lambda : sys.stdin.readline().rstrip()

stak = list()
N = int(input())
for i in range(N):
    command, *x = input().split()
    if command == "push":
        stak.append(int(x[0]))
    elif command == "pop":
        if len(stak) != 0:
            print(stak.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stak))
    elif command == "empty":
        if len(stak) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(stak) != 0:
            print(stak[-1])
        else:
            print(-1)
    else:
        print("Wrong Command!!")
        i=i-1