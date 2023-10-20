N = int(input().rstrip())
list_ = []
for i in range(N):
    list_.append(list(map(int, input().split(" "))))
check = []
winner = []
grade = 3

list_.sort(key = lambda x : -x[2])
for i in list_:
    if i[0] not in check or check.count(i[0]) < 2:
        check.append(i[0])
        winner.append(i)
        grade -= 1
    if grade == 0:
        break

for i in winner:
    print(i[0], i[1])