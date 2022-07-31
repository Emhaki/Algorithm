a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a와b의 점수
a_score = 0
b_score = 0
# 점수가 계속 똑같다면 latest_winner은 "D"로 설정
latest_winner = "D"

# 라운드당 1번씩 10번 반복
for i in range(10):
    if a[i] > b[i]:
        a_score += 3
        latest_winner = "A"
    elif a[i] < b[i]:
        b_score += 3
        latest_winner = "B"
    elif a[i] == b[i]:
        a_score += 1
        b_score += 1

# 점수를 통해 if 비교문
if a_score > b_score:
    print(a_score, b_score)
    print("A")
elif a_score < b_score:
    print(a_score, b_score)
    print("B")
elif a_score == b_score:
    print(a_score, b_score)
    print(latest_winner)
elif latest_winner != "A" or latest_winner != "B":
    print(a_score, b_score)
    print(latest_winner)