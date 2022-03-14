import sys
input = lambda : sys.stdin.readline().rstrip()

numbers=[]
while True:
    num = int(input())
    if num== 0:
        break
    numbers.append(num)


for num in numbers:
    count = 0
    flag = [False,False] + [True]*(2*num-1)
    for i in range(2, num*2 + 1):
        if flag[i]:
            if i>num and i<=2*num:
                count += 1
            for j in range(2*i, num*2 + 1, i):
                flag[j] = False
    print(count)