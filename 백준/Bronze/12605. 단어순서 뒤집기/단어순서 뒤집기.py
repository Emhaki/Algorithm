for _ in range(int(input())):
  list_ = list(map(str, input().split()))
  list_.reverse()
  print(f'Case #{_+1}:',' '.join(list_))