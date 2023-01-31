import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    queue = deque()
    queue.append((r1,c1))
    visited[r1][c1] = 1

    while queue:
        x, y = queue.popleft()

        # 6가지 이동 방법
        for i in range(6):
            nx = dx[i] + x 
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

visited = [[0] * N for _ in range(N)]

bfs()

print(visited[r2][c2] - 1)