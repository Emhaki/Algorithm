N = input().split('-')
num = []
for i in N:
  cnt = 0
  result = i.split('+') # +를 기준으로 한번 더 split
  for j in result:
    cnt += int(j)
  num.append(cnt)
n = num[0]
for i in range(1, len(num)):
  n -= num[i]
print(n)