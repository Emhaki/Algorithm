from heapq import heappop, heapify, heappush
N, M = map(int, input().split(" "))
card_list = list(map(int, input().split(" ")))

heapify(card_list)
for _ in range(M):
    x = heappop(card_list)
    y = heappop(card_list)
    heappush(card_list, x+y)
    heappush(card_list, x+y)

print(sum(card_list))