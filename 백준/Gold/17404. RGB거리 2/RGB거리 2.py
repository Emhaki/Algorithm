import sys
input = sys.stdin.readline

N = int(input())

house = [list(map(int, input().split())) for _ in range(N)]
INF = sys.maxsize

answer = INF
for i in range(3):
    dp = [[INF, INF, INF] for _ in range(N)]
    dp[0][i] = house[0][i]

    for j in range(1, len(house)):
        dp[j][0] = house[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = house[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = house[j][2] + min(dp[j-1][0], dp[j-1][1])
    
    for k in range(3):
        if i != k:
            answer = min(answer, dp[-1][k])

print(answer)