import sys
input = sys.stdin.readline

from collections import deque

R, C = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

dx, dy = [0,0,-1,1], [-1,1,0,0]

def bfs(i,j, sheep, wolf):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1 # 방문처리

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 > nx or nx >= R or 0 > ny or ny >= C:
                continue
            
            if graph[nx][ny] == 'v' and visited[nx][ny] == 0: # 늑대일때
                wolf += 1
                visited[nx][ny] = 1
                queue.append((nx,ny))
            
            if graph[nx][ny] == 'o' and visited[nx][ny] == 0: # 양일때
                sheep += 1
                visited[nx][ny] = 1
                queue.append((nx,ny))

            if graph[nx][ny] == '.' and visited[nx][ny] == 0: # 공간일때
                visited[nx][ny] = 1
                queue.append((nx,ny))
    if wolf >= sheep:
        sheep = 0
    elif wolf < sheep:
        wolf = 0
    return [wolf, sheep]

wolf_result = 0
sheep_result = 0
all_result = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'v' and visited[i][j] == 0:
            wolf = 1
            sheep = 0
            all_result = bfs(i,j, sheep, wolf)
            wolf_result += all_result[0]
            sheep_result += all_result[1]
        if graph[i][j] == 'o' and visited[i][j] == 0:
            wolf = 0
            sheep = 1
            all_result = bfs(i,j, sheep, wolf)
            wolf_result += all_result[0]
            sheep_result += all_result[1]
            
print(sheep_result, wolf_result)