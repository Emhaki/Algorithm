import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().split())

MAX = 100001
visited = [-1] * MAX
visited[N] = 0 # 수빈이의 위치 방문처리

queue = deque()
queue.append(N)

while queue:
    x = queue.popleft()
    
    if x == K:
        print(visited[x])
        break

    for j in (x - 1), (x + 1), (x * 2): # 그냥 이동일때는 시간 추가
        if 0 <= j < MAX:
            if visited[j] == -1 and j == (x * 2) and j != 0: # 방문하지 않았거나, 순간이동값이거나, 0이 아니라면
                visited[j] = visited[x] # 시간 그대로
                queue.appendleft(j)
            elif visited[j] == -1 and (j == (x - 1) or j == (x + 1)): # 걷는거라면
                visited[j] = visited[x] + 1
                queue.append(j)