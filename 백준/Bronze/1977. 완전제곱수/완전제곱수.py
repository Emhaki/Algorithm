M = int(input())
N = int(input())
double_list = []
result_list = []
for i in range(1000):
    double_list.append(i*i)
for j in double_list:
    if M <= j <= N:
        result_list.append(j)
if len(result_list) > 0:
    print(sum(result_list))
    print(min(result_list))
else:
    print(-1)
