from itertools import *
N, M = map(int, input().split())
list_ = list(map(int, input().split()))
result_list = list(product(sorted(list_), repeat=M))
for i in result_list:
  print(*i)