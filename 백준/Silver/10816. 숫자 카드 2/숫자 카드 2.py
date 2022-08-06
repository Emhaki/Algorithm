import sys
n = int(input())
card_1 = list(map(int, sys.stdin.readline().split()))
m = int(input())
card_2 = list(map(int, sys.stdin.readline().split()))
res = dict()

for i in card_1:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

for i in card_2:
    if i in res:
        print(res[i], end=' ')
    else:
        print(0, end=' ')
