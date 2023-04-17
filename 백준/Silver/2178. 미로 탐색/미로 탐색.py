import sys
input = sys.stdin.readline

from collections import deque
# N, M 정수
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()

def bfs(i,j):
    queue.append((i,j))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1 and visited[nx][ny] == 0:
                graph[nx][ny] = 0 # 지나간길 없애기
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
    
    return visited[-1][-1]


print(bfs(0,0) + 1)