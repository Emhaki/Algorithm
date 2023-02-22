import sys
input = sys.stdin.readline

from itertools import permutations

N = int(input())
num_list = list(map(int, input().split()))
num = permutations(num_list)

result = 0
for i in num:
    mid_sum = 0
    for j in range(N-1):
        mid_sum += abs(i[j] - i[j-1])
    result = max(mid_sum, result)

print(result)