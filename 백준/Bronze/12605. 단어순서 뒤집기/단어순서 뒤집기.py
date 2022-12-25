from collections import deque
N = int(input())
for _ in range(N):
  list_ = []
  list_ = list(map(str, input().split()))
  list_ = deque(list_)
  list_.reverse()
  print(f'Case #{_+1}:',' '.join(list_))