n = int(input())
A = list(map(int,input().split()))
dp = [0]*1001

for i in A:
    dp[i] = max(dp[:i])+i
print(max(dp))