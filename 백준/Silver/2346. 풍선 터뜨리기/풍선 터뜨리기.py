from collections import deque
N = int(input())

deq = deque(enumerate(map(int, input().split())))
result = []
# [3 2 1 -3 -1]
while deq:
    idx, paper = deq.popleft()
    result.append(idx + 1)

    if paper > 0:
        deq.rotate(-(paper - 1))
    elif paper < 0:
        deq.rotate(-paper)

print(*result)