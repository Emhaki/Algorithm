list_ = list(map(int, input().split()))
cnt = 0
for i in list_:
    cnt += (i * i)
print(cnt % 10)