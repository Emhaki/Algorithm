import sys
input = sys.stdin.readline

N = int(input())
boxes = list(map(int, input().split()))
dp = [1] * N # 시작이 1이므로

for i in range(1, N):
    for j in range(i):
        if boxes[i] > boxes[j]: # 앞에 상자가 뒷 상자보다 클 경우
            dp[i] = max(dp[i], dp[j] + 1) # 앞 상자에 현재값과 상자의 수 + 1중 큰 값 저장

print(max(dp))