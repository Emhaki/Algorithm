day = int(input())
list_ = list(map(int, input().split()))
cnt = 0
for i in list_:
    if i == day:
        cnt += 1
print(cnt)