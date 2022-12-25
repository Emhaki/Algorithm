from itertools import *
N, M = map(int, input().split())
list_ = list(map(int, input().split()))
result_list = list(combinations_with_replacement(sorted(list_), M))
for i in result_list:
  print(*i)