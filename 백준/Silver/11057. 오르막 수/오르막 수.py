import sys
input = sys.stdin.readline

N = int(input())
dp = [1 for _ in range(10)]

for i in range(N-1):
    for j in range(10):
        dp[j] = sum(dp[j:])

print(sum(dp) % 10007)