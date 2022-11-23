N = input()
str(N)
list_ = []
for i in N:
  list_.append(int(i))
k = ""
for j in sorted(list_, reverse=True):
  k += str(j)

print(int(k))