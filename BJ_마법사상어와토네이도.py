import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
# n/2부터 시작
r, c = n // 2, n // 2

per_left = [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, "alpa", 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]
per_down = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, "alpa", 10, 0], [0, 0, 5, 0, 0]]
per_right = [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, "alpa", 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]]
per_up = [[0, 0, 5, 0, 0], [0, 10, "alpa", 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

vector = [[0, -1], [1, 0], [0, 1], [-1, 0]]


def cal_sand(a, b, A_array, rate_list, ot_sand):
    x, y = r - 2, c - 2  # rate_list랑 인덱스 맞춰주기 위해서
    spread_sand = 0  # 퍼진 모래양 표시하기 위해서
    a_x, a_y = 0, 0  # 알파의 인덱스를 담아두기 위한 변수
    for i in range(5):
        for j in range(5):
            if rate_list[i][j] == 0:  # 퍼지는 모래가 없으면 넘어가기
                continue
            elif rate_list[i][j] != "alpa":  # 퍼지는 모래가 있으면
                if -1 < i + x < n and -1 < j + y < n:  # 격자 안이면
                    A_array[i + x][j + y] += (A_array[a][b] * rate_list[i][j] // 100)
                else:  # 격자 밖일 경우
                    ot_sand += (A_array[a][b] * rate_list[i][j] // 100)
                spread_sand += (A_array[a][b] * rate_list[i][j] // 100)
            else:  # 알파일 경우
                a_x, a_y = i, j

    if -1 < a_x + x < n and -1 < a_y + y < n:  # 알파가 격자 안일 경우
        A_array[a_x + x][a_y + y] += (A_array[a][b] - spread_sand)
    else:  # 알파가 격자 밖일 경우
        ot_sand += (A_array[a][b] - spread_sand)
    A_array[a][b] = 0  # 모래를 다나눠줬으니 제로
    return ot_sand, A_array


out_sand = 0  # 격자 밖으로 나간 모래의 양
cnt = 1
flag = 0
while flag == 0:
    for i in range(4):  # 왼, 아래, 오른, 위 반복
        for j in range(cnt):  # 방향 몇번 반복?
            r += vector[i][0]  # 해당 방향으로 이동한 좌표
            c += vector[i][1]  # =
            if -1 < r < n and -1 < c < n:
                if A[r][c] == 0:  # 모래가 없으면 Pass
                    continue
                elif i == 0:  # 왼
                    out_sand, A = cal_sand(r, c, A, per_left, out_sand)
                    # print(out_sand)
                elif i == 1:  # 아래
                    out_sand, A = cal_sand(r, c, A, per_down, out_sand)
                    # print(out_sand)
                elif i == 2:  # 오
                    out_sand, A = cal_sand(r, c, A, per_right, out_sand)
                    # print(out_sand)
                elif i == 3:  # 위
                    out_sand, A = cal_sand(r, c, A, per_up, out_sand)
                    # print(out_sand)
            else:
                flag = 1
                break

        if i == 1 or i == 3:
            cnt += 1

        if flag == 1:
            print(out_sand)
            break
