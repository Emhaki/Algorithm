import sys
input = sys.stdin.readline
from collections import deque
T = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i,j):
    visited = [[0] * W for _ in range(H)]
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0 and graph[nx][ny] == '#':
                visited[nx][ny] = 1
                graph[nx][ny] = '.'
                queue.append((nx, ny))
    
for _ in range(T):
    H, W = map(int, input().split())
    graph = [list(input().strip()) for _ in range(H)] # 띄어쓰기 구분이 아닐때 입력형식
    cnt = 0
    for i in range(H):
        for j in range(W):
            if graph[i][j] == '#':
                bfs(i,j)
                cnt += 1

    print(cnt)