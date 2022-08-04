N = int(input())
s = []

for _ in range(N):
    s.append(list(map(str, input())))  # 리스트로 append
# s =[['.', '.', '.', '.', 'X'],
    # ['.', '.', 'X', 'X', '.'],
    # ['.', '.', '.', '.', '.'],
    # ['.', 'X', 'X', '.', '.'],
    # ['X', '.', '.', '.', '.']]


row_place, col_place = 0, 0  # 가로 누울 공간, # 세로 누울 공간
for i in range(N):
    row_count = 0  # .의 갯수
    com_count = 0  # .의 갯수
    for j in range(N):
        if s[i][j] == '.':
            row_count += 1
        elif s[i][j] == 'X':
            if row_count >= 2:
                row_place += 1
            row_count = 0

        if s[j][i] == '.':
            com_count += 1
        elif s[j][i] == 'X':
            if com_count >= 2:
                col_place += 1
            com_count = 0

        if j == N-1:
            if row_count >= 2:
                row_place += 1
                row_count = 0
            if com_count >= 2:
                col_place += 1
                com_count = 0


print(row_place, col_place)