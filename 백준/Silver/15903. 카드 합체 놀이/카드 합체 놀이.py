N, M = map(int, input().split(" "))
card_list = list(map(int, input().split(" ")))

for _ in range(M):
    idx = card_list.pop(card_list.index(min(card_list)))
    idx2 = card_list.pop(card_list.index(min(card_list)))
    new_number = idx + idx2
    card_list.append(new_number)
    card_list.append(new_number)

print(sum(card_list))