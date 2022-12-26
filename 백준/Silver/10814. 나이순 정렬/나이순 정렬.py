N = int(input())
list_ = []
for _ in range(N):
  age, name = input().split()
  list_.append([int(age), name])
list_.sort(key=lambda x:int(x[0]))
for i in list_:
  print(i[0], i[1])