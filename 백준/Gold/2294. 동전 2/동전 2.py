import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
INF = sys.maxsize
for _ in range(n):
    coins.append(int(input()))

dp = [INF] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])