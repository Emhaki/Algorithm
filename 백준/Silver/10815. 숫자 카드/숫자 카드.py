N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
card_list2 = list(map(int, input().split()))

dict_ = {}
for i in range(len(card_list)):
  dict_[card_list[i]] = 0

for j in range(M):
  if card_list2[j] not in dict_:
    print(0, end=' ')
  else:
    print(1, end=' ')