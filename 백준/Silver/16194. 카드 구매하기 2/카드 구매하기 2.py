import sys
input = sys.stdin.readline

from copy import deepcopy
N = int(input())
card_list = [0] + list(map(int, input().split()))
dp = deepcopy(card_list)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + card_list[j])

print(dp[-1])