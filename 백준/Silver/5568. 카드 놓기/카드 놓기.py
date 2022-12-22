from itertools import *
N = int(input())
K = int(input())
list_ = [input() for _ in range(N)]
res = set()
for i in permutations(list_, K):
  res.add(''.join(i))
print(len(res))