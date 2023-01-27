import sys
input = sys.stdin.readline

from collections import deque
N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
dx, dy = [0,0,-1,1], [-1,1,0,0]
queue = deque()
queue.append((0,0))
visited[0][0] = 1

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

print(visited[N-1][M-1])