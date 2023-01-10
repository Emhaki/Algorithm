n, k = map(int, input().split())
grade = []
for _ in range(n):
  list_ = list(map(int, input().split()))
  grade.append(list_)

grade = sorted(grade, key = lambda x : (-x[1], -x[2], -x[3]))

idx = []
for i in grade:
  if i in grade:
    idx.append(i)

for i in grade:
  if i[0] == k:
    idx = i

# [[1, 3, 0, 0], [4, 0, 2, 0], [2, 0, 2, 0], [3, 0, 0, 2]]
print(grade.index(idx))