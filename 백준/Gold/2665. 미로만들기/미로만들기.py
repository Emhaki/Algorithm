import sys
input = sys.stdin.readline

from collections import deque

# N 세로, M 가로, K 개수
N = int(input())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
queue = deque()

def bfs():
    visited[0][0] = 0
    queue.append((0,0))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                else:
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx,ny))
                
bfs()
print(visited[N-1][N-1])