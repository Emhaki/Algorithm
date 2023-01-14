while True:
  list_ = sorted(list(map(int, input().split())))
  if sum(list_) == 0:
    break

  if list_[0]**2 + list_[1]**2 == list_[2]**2:
      print('right')
  else:
      print('wrong')