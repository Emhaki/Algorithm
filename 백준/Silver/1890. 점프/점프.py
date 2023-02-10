import sys
input = sys.stdin.readline
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

# 반복문으로 그래프의 좌표 탐색
for i in range(N):
    for j in range(N):
        
        # 마지막 값 출력
        if i == N-1 and j == N-1:
            print(dp[i][j]) # 마지막 값
            break
        
        jump = board[i][j] # 점프 값

        # 아래쪽 방향
        if i + jump < N:
            dp[i + jump][j] += dp[i][j]
        
        # 오른쪽 방향
        if j + jump < N:
            dp[i][j + jump] += dp[i][j]