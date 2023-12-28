import sys
input = sys.stdin.readline

from heapq import heappop, heappush
N = int(input().strip())
result = []

for _ in range(N):
    number = int(input().strip())
    if number > 0:
        heappush(result, number)
    elif number == 0:
        if not result:
            print(0)
        else:
            print(heappop(result))