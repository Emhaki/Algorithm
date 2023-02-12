import sys
input = sys.stdin.readline
N = int(input())

dp = [-1] * 10001
# 1은 상근, 2는 창용 승
dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, N+1):
    if dp[i-1] == 1 or dp[i-3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1

if dp[N] == 1:
    print('CY')
else:
    print('SK')