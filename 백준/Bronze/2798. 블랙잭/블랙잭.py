N, M = map(int, input().split())
card_list = list(map(int, input().split()))
# card_list = [5, 6, 7, 8, 9]

number_list = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card_list[i]+card_list[j]+card_list[k] <= M:
                number_list.append(card_list[i]+card_list[j]+card_list[k])
print(max(number_list))