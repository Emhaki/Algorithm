import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1,0]
dy = [0,1]
def bfs(x,y):
    queue = deque()
    queue.append([x,y])

    while queue:
        x, y = queue.popleft()
        step = board[x][y]

        if board[x][y] == -1:
            return True

        for i in range(2):
            nx = x + dx[i] * step # 좌표만큼 점프
            ny = y + dy[i] * step

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append([nx,ny])


if bfs(0,0): # True라면
    print('HaruHaru')
else:
    print('Hing')