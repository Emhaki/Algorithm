import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [0,0,-1,1], [-1,1,0,0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1 # 방문처리
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1 # 방문처리
                cnt += 1
                queue.append((nx,ny))
    return cnt         

painting = 0 # 그림의 갯수
result = 0 # 그림의 최대 넓이
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            result = max(bfs(i,j), result)
            painting += 1

print(painting)
print(result)