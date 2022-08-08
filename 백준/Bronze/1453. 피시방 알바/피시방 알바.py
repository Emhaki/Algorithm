N = int(input())
customer = {}
list_ = list(map(int, input().split()))
for i in list_:
    if i not in customer:
        customer[i] = 1
    else:
        customer[i] += 1
cnt = 0
for k, v in customer.items():
    if v > 1:
        cnt += v-1
print(cnt)