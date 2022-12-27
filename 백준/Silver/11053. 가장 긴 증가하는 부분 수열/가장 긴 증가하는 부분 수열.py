import bisect
N = int(input())
list_ = list(map(int, input().split()))

dp = [list_[0]]

for i in range(N):
    if list_[i] > dp[-1]:
        dp.append(list_[i])
    else:
        idx = bisect.bisect_left(dp, list_[i])
        dp[idx] = list_[i]

print(len(dp))