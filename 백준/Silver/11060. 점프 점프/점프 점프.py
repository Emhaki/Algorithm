import sys
input = sys.stdin.readline

N = int(input())
jump_list = list(map(int, input().split()))
dp = [-1] * N
dp[0] = 0

for current in range(0, N-1):
    if dp[current] == -1:
        continue
    
    for next_step in range(1, jump_list[current] + 1):
        if current + next_step >= N:
            break
        if dp[current + next_step] == -1 or dp[current + next_step] > dp[current] + 1:
            dp[current + next_step] = dp[current] + 1

print(dp[N-1])