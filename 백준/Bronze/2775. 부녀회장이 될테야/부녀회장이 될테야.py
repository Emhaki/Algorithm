T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [_ for _ in range(1, n+1)]
    for i in range(k): # 층 수만큼
        for j in range(1, n): # 1 ~ n-1까지
            dp[j] += dp[j-1] 

    print(dp[-1])
# 3층 1 5 15 40 70
# 2층 1 4 10 20 35
# 1층 1 3 6 10 15
# 0층 1 2 3 4 5