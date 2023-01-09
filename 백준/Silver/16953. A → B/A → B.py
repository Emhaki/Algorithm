n, m = map(int, input().split())
r = 1
while (m != n):
  r += 1
  temp = m
  if m % 10 == 1:
    m //= 10
  elif m % 2 == 0:
    m //= 2
  
  if temp == m:
    print(-1)
    break
else:
  print(r)