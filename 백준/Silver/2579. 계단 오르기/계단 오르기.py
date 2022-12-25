# 한 번 또는 두 계단씩
# 연속으로 세 계단은 x
# 마지막 계단은 무조건 밟아야 함
cnt = int(input())
list_ = [ int(input()) for _ in range(cnt)]
dp = [0] * cnt

if len(list_) <= 2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
  print(sum(list_))
else:
  dp[0] = list_[0]
  dp[1] = list_[0] + list_[1]
  for i in range(2, cnt): # 세번째 계단부터 dp 점화식을 이용해 최댓값 구하기
    dp[i] = max(list_[i] + list_[i-1] + dp[i-3], list_[i]+dp[i-2])
  print(dp[cnt-1])