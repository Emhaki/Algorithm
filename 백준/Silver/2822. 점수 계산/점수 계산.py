list_ = []
index_list = []
for _ in range(8):
  list_.append(int(input()))

k = sorted(list_, reverse=True)
result = sum(k[:5])
for i in k[0:5]:
  index_list.append(list_.index(i)+1)
print(result)
print(*sorted(index_list))