import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().split())

MAX = 100001
visited = [-1] * MAX
visited[N] = 0 # 수빈이의 위치 방문처리

queue = deque()
queue.append(N)

time = 0
way = 0

while queue:
    x = queue.popleft()
    count = visited[x]
    if x == K:
        time = count
        way += 1
        continue

    for j in (x - 1), (x + 1), (x * 2):
        if 0 <= j < MAX:
          if visited[j] == -1 or visited[j] == visited[x] + 1: # 방문하지 않았거나, 방문했더라도 x까지 시간 + 1과 같다면
            visited[j] = count + 1 # 시간 기록
            queue.append(j)

print(time)
print(way)