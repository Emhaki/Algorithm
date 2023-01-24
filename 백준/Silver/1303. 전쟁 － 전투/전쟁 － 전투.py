import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())

graph = [list(str(input().strip())) for _ in range(M)]
result = [0, 0]
# 
# [
# ['W', 'B', 'W', 'W', 'W'],
# ['W', 'W', 'W', 'W', 'W'], 
# ['B', 'B', 'B', 'B', 'B'], 
# ['B', 'B', 'B', 'W', 'W'], 
# ['W', 'W', 'W', 'W', 'W']
# ]

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
def bfs(x, y, a):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 'X'
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == a:
                graph[nx][ny] = 'X'
                cnt += 1
                queue.append((nx, ny))
    return cnt * cnt

for i in range(M):
    for j in range(N):
        if graph[i][j] == "W":
            result[0] += bfs(i,j, "W")
        elif graph[i][j] == "B":
            result[1] += bfs(i,j, "B")

print(*result)