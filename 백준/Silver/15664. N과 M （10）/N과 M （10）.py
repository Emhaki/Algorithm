import sys
input = sys.stdin.readline

from itertools import combinations
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
num = combinations(num_list, M)
result = []
for i in num:
    result.append(i)
  
result = sorted(list(set(result)))

for i in result:
    for j in i:
        print(j, end=' ')
    print()