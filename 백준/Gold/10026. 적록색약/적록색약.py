import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
graph = [list(map(str, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i,j, color):
    queue = deque()
    queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        if visited[x][y] == 0:
            visited[x][y] = 1
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == color:
                        queue.append((nx,ny))

local = 0
local2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color = graph[i][j]
            bfs(i,j,color)
            local += 1

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            color = graph[i][j]
            bfs(i,j,color)
            local2 += 1

print(local, local2)