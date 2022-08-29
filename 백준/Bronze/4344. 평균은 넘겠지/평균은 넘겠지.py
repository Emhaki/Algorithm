import math

C = int(input())
result_list = []
for _ in range(C):
    average = list(map(int, input().split()))
    count = 0
    average.pop(0)
    result = sum(average)/len(average)
    for i in average:
        if i > result:
            count += 1

    result_list.append(count/len(average) * 100)

for j in result_list:
    print('%.3f' % j+'%')