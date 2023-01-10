n = int(input())
a, b = 0, 1
for i in range(n):
  a, b = b, a+b # a와 b를 계속해서 갱신시켜서 점화식이 성립하게끔

print(a)