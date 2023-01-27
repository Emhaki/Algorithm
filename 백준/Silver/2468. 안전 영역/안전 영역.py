import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
high = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] > high:
            high = graph[i][j] # 최대높이 저장

dx, dy = [0,0,-1,1], [-1,1,0,0]
queue = deque()
def bfs(i,j,high):
    queue.append((i,j))
    visited[i][j] = 1 # 방문처리

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] > high and visited[nx][ny] == 0:
                visited[nx][ny] = 1 # 방문처리
                queue.append((nx, ny))                

result = 0
for k in range(high):
  visited = [[0] * N for _ in range(N)]
  cnt = 0

  for i in range(N):
      for j in range(N):
          if graph[i][j] > k and visited[i][j] == 0:
              bfs(i,j, k)
              cnt += 1

  if result < cnt: # cnt가 더 클때마다 result에 저장
      result = cnt

print(result)