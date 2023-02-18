import sys
input = sys.stdin.readline
N, K = map(int, input().split())
bag = [(0,0)] # 인덱스 0자리 차지하기

for _ in range(N):
    W, V = map(int, input().split())
    bag.append((W,V))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = bag[i] # 인덱스 1부터 꺼내기
    for j in range(1, K+1):
        if (j - W) < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)

print(dp[N][K])