import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
result = set(permutations(num_list, m))
answer = []
result = sorted(result, reverse=False)
for i in result:
      print(*i)