N = int(input())
dic_ = {}

for _ in range(N):
    card_number = int(input())
    if card_number not in dic_:
        dic_[card_number] = 1
    else:
        dic_[card_number] += 1
# dic_ = {1: 3, 2: 2}
many_card = max(dic_.values())
list_ = []
for k, v in dic_.items():
    if v == many_card:
        list_.append(k)
print(min(list_))