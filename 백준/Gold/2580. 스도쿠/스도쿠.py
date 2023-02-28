import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(9)]

# 행 별로 들어가 있는 숫자 / i번 행에 j가 들어가 있는지
row = [[False] * 9 for _ in range(9)]
# 열 별로 들어가 있는 숫자 / i번 열에 j가 들어가 있는지
col = [[False] * 9 for _ in range(9)]
# 박스 별로 들어가 있는 숫자 / i번 박스에 j가 들어가 있는지
box = [[False] * 9 for _ in range(9)]


def square(i,j):
    return (i//3)*3+(j//3)

for i in range(9):
    for j in range(9):
        if board[i][j]: # 인덱스가 0이 아니라면
            row[i][board[i][j]-1] = True
            col[j][board[i][j]-1] = True
            box[square(i,j)][board[i][j]-1] = True

def back(i,j):
    if i == 9:
        for i in board:
            print(*i)
        exit(0)

    if board[i][j]:
        back(i + (j+1)//9, (j+1) % 9) # 9를 넘지 않도록
        return
    
    for k in range(9):
        if row[i][k] or col[j][k] or box[square(i,j)][k]:
            continue
        board[i][j] = k + 1
        row[i][k] = True
        col[j][k] = True
        box[square(i,j)][k] = True

        back(i + (j+1)//9, (j+1) % 9)
        board[i][j] = 0 # 다시 원상복구
        row[i][k] = False
        col[j][k] = False
        box[square(i,j)][k] = False

back(0,0)