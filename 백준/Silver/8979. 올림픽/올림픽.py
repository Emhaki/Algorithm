n, k = map(int, input().split())
grade = []
for _ in range(n):
  list_ = list(map(int, input().split()))
  grade.append(list_)

grade = sorted(grade, key = lambda x : (-x[1], -x[2], -x[3]))

for i in range(n):
  if grade[i][0] == k:
    idx = i

for i in range(n):
  if grade[idx][1:] == grade[i][1:]:
    print(i + 1)
    break