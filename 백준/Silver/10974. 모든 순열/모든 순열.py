import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
num_list = []
for i in range(1, N+1):
    num_list.append(i)

num = permutations(num_list)
for j in num:
    print(*j)