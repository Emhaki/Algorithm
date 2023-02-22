import sys
input = sys.stdin.readline

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(float(input()))

dp = [0] * n
dp[0] = num_list[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]*num_list[i], num_list[i])

print('%0.3f' % max(dp))