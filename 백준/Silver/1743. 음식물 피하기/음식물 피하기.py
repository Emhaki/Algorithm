import sys
input = sys.stdin.readline

from collections import deque

# N 세로, M 가로, K 개수
N, M, K = map(int, input().split())

graph = [['.'] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
queue = deque()
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 음식물 그래프 삽입
trash = []
for i in range(K):
    a, b = map(int, input().split())
    trash.append((a,b))
for x, y in trash:
    graph[x-1][y-1] = '#'

# bfs 생성
def bfs(i,j):
    visited[i][j] = True
    queue.append((i,j))
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False and graph[nx][ny] == '#':
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx, ny))

    return cnt

result = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == '#':
            result.append(bfs(i,j))

print(max(result))