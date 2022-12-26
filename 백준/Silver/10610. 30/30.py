N = list(input())
N.sort(reverse=True) # ['8', '8', '7', '5', '5', '4', '2', '0']
sum = 0
for i in N:
  sum += int(i) # 각 자리수를 더했을 때 3으로 나누어 떨어져야 함
if sum % 3 != 0 or '0' not in N: # 3으로 나누어지지 않거나, 0이 포함되어 있지 않으면 30의 배수 x
  print(-1)
else:
  print("".join(N))