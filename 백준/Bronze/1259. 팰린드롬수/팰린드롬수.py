while True:
  list_ = int(input())
  li = []
  if list_ == 0:
    break
  list_ = str(list_)
  for i in list_:
    li.append(i)
  k = list(reversed(li))
  if li == k:
      print('yes')
  else:
      print('no')