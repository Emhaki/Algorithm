import sys
input = sys.stdin.readline

from collections import deque
R, C = map(int, input().split())

graph = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i,j,sheep,wolf):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            
            if graph[nx][ny] == 'v' and visited[nx][ny] == 0:
                wolf += 1
                visited[nx][ny] = 1
                queue.append((nx,ny))
            if graph[nx][ny] == 'k' and visited[nx][ny] == 0:
                sheep += 1
                visited[nx][ny] = 1
                queue.append((nx,ny))

            if graph[nx][ny] == '.' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
    if wolf >= sheep:
        sheep = 0
    elif wolf < sheep:
        wolf = 0
    
    return [sheep, wolf]

wolf_result = 0
sheep_result = 0
all_result = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'v' and visited[i][j] == 0:
            sheep = 0
            wolf = 1
            all_result = bfs(i,j,sheep,wolf)
            sheep_result += all_result[0]
            wolf_result += all_result[1]
        if graph[i][j] == 'k' and visited[i][j] == 0:
            sheep = 1
            wolf = 0
            all_result = bfs(i,j,sheep,wolf)
            wolf_result += all_result[1]
            sheep_result += all_result[0]

print(sheep_result, wolf_result)