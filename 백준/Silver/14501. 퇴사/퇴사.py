N = int(input())
dp_list = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if i + dp_list[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i + dp_list[i][0]] + dp_list[i][1])

print(dp[0])