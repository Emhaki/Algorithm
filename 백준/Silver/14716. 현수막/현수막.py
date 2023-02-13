import sys
input = sys.stdin.readline
from collections import deque
M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]
visited = [[-1] * N for _ in range(M)]

# 상 우상 우 우하 하 좌하 좌 좌상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
queue = deque()

def bfs(i,j):
    queue.append((i,j))
    visited[i][j] = 0 # 방문처리

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = 0 # 방문처리
                queue.append((nx,ny))

word = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == -1:
            bfs(i,j)
            word += 1

print(word)