import sys
input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(R)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs():
    j_queue = deque()
    f_queue = deque()
    
    j_time = [[0] * C for _ in range(R)]
    f_time = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'J':
                j_queue.append((i, j))
                j_time[i][j] = 1

            elif graph[i][j] == 'F':
                f_queue.append((i, j))
                f_time[i][j] = 1

    while f_queue:
        x, y = f_queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < R and 0 <= ny < C:
                if not f_time[nx][ny] and graph[nx][ny] != '#':
                    f_time[nx][ny] = f_time[x][y] + 1
                    f_queue.append((nx, ny))
    
    while j_queue:
        x, y = j_queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < R and 0 <= ny < C:
                if not j_time[nx][ny] and graph[nx][ny] != '#':
                    if not f_time[nx][ny] or f_time[nx][ny] > j_time[x][y] + 1:
                        j_time[nx][ny] = j_time[x][y] + 1
                        j_queue.append((nx,ny))
            
            else:
                return j_time[x][y]

    return 'IMPOSSIBLE'

print(bfs())