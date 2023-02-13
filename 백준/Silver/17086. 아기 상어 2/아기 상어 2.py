import sys
input = sys.stdin.readline

from collections import deque
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


# 상 우상 우 우하 하 좌하 좌 좌상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited = [[0] * M for _ in range(N)]
    visited[i][j] = 1 # 방문처리

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

                if graph[nx][ny] == 1:
                    return visited[nx][ny]-1
    
result = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
              result.append(bfs(i,j))

print(max(result))