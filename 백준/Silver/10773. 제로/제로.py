N = int(input())
list_ = []
result = []
for i in range(N):
  list_.append(int(input()))

for k in list_:
  if k != 0:
    result.append(k)
  else:
    result.pop()
print(sum(result))