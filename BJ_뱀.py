import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
K = int(input())
apple=[]
for _ in range(K): # 사과의 위치정보
    n, m = map(int, input().split())
    apple.append((n,m))

L = int(input())
s_pos = [0]
for _ in range(L): #뱀의 방향전환 정보
    x, c = input().split()
    s_pos.append((int(x), c))

dn = [0,-1,0,1] #오위왼아 -> 왼쪽으로 90도 회전 = +1
dm = [1,0,-1,0]
map = [[0]*N for _ in range(N)]
for pos in apple:
    map[pos[0]-1][pos[1]-1] = "A" #사과가 있다고 표시

snake = [(0,0)] #0위치, 1몸길이, 2방향, 3회전횟수
map[0][0] = 1
start_time = 0
current_cnt = 0
go = 0

while True:
    start_time += 1
    head = snake[0] #머리는 몸위치 리스트의 젤앞
    tail = snake[-1] #꼬리는 몸위치 리스트의 젤끝
    # head가 갈 다음 위치 좌표 계산
    nn = head[0] + dn[go]
    nm = head[1] + dm[go]

    if -1<nn<N and -1<nm<N and map[nn][nm] != 1: #이동할 위치가 벽이나 자신의 몸이 있는곳이 아니라면
        snake.insert(0, (nn, nm))#머리 새로 추가
        if map[nn][nm] != "A":# 사과를 못먹었을 경우에
            map[tail[0]][tail[1]] = 0 #원래 꼬리 위치는 지워주기
            snake.pop()#젤 마지막 요소 삭제
        map[nn][nm] = 1
    else:
        print(start_time)
        break

    #cnt=1부터 시작
    if current_cnt != L:
        if s_pos[current_cnt+1][0] == start_time:  # 해당 실행시간에 뱀의 방향이 바뀔 정보가 있다면
            c = s_pos[current_cnt+1][1]
            if c == "L":
                go = (go + 1) % 4
            elif c == "D":
                go = abs((go - 1) % 4)
            current_cnt += 1