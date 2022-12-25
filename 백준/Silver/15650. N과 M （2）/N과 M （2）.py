from itertools import *
N, M = map(int, input().split())
list_ = [ _ for _ in range(1, N+1)]
result_list = list(combinations(list_, M))
for i in result_list:
  print(*i)