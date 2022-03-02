import sys
input = lambda : sys.stdin.readline().rstrip()

num_tc = int(input())
fly_info = [list(map(int, input().split())) for _ in range(num_tc)]

for x, y in fly_info:
    distance = y - x
    count = 0
    move = 1
    move_plus = 0
    while move_plus < distance :
        count += 1
        move_plus += move
        if count % 2 == 0 : # count가 2의 배수일 때,
            move += 1
    print(count)