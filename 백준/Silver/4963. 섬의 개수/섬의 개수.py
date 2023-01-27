import sys
input = sys.stdin.readline

from collections import deque
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def bfs(i, j):
    queue = deque()
    graph[i][j] = 0
    queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(h)]

    if w + h == 0:
        break
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)