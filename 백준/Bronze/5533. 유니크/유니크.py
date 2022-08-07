N = int(input())
first_game = []
second_game = []
third_game = []
for _ in range(N):
    a, b, c = list(map(int, input().split()))
    first_game.append(a)
    second_game.append(b)
    third_game.append(c)
result_game = [first_game, second_game, third_game]  # 2차원배열 형태로 변환

score = [0] * N  # [0, 0, 0, 0, 0]
for i in range(3):
    for j in range(N):
        # 같은 수가 2개 이상이면 0점
        if result_game[i].count(result_game[i][j]) >= 2:
            score[j] == 0
        else:  # 같은 수가 없으면 점수 획득
            score[j] += result_game[i][j]

for s in score:
    print(s)