import sys


N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for i in range(N)]
count = []

for i in range(N-7):
    for j in range(M-7):
        count_1 = 0  #만약 시작을 W로 칠할 경우 바꿔야할 칸 개수
        count_2 = 0  #만약 시작을 B로 칠할 경우 바꿔야할 칸 개수

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        count_1 += 1
                    if board[k][l] != 'B':
                        count_2 += 1
                else:
                    if board[k][l] != 'B':
                        count_1 += 1
                    if board[k][l] != 'W':
                        count_2 += 1

        count.append(min(count_1, count_2)) #두가지 경우에서 작은 경우를 추가

print(min(count))