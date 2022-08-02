import heapq
import sys

n = int(input())
heapq_list = []

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(heapq_list, (abs(a), a))
    else:
        if not heapq_list:
            print(0)
        else:
            print(heapq.heappop(heapq_list)[1])