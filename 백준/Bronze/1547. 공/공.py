M = int(input())
ball = [0, -1, -1]

for _ in range(M):
    X, Y = map(int, input().split())
    temp = 77 # 저장할 임시값 선언
    temp = ball[X-1] # 첫번째 컵을 임시값에 저장
    ball[X-1] = ball[Y-1] # 두번째 컵을 첫번째 컵에 저장
    ball[Y-1] = temp # 임시값을 두번째 컵으로 저장
print(ball.index(0)+1)
