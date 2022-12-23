list_ = [int(input()) for _ in range(4)]
result = sum(list_)
cnt = 0
while result >= 60:
  result -= 60
  cnt += 1
print(cnt)
print(result)