import sys
input = sys.stdin.readline

from heapq import heappop, heappush
INF = sys.maxsize

dx = [0,0,-1,1]
dy = [-1,1,0,0]

M, N = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[INF] * M for _ in range(N)]

def daikstar():
    queue = []
    heappush(queue, (0,0,0)) # 삽입
    visited[0][0] = 0

    while queue:
        cost, x, y = heappop(queue) # 할당
        
        if cost > visited[x][y]:
            continue
            
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if cost + graph[nx][ny] < visited[nx][ny]:
                visited[nx][ny] = cost + graph[nx][ny]
                heappush(queue, (visited[nx][ny], nx, ny))

daikstar()
print(visited[N-1][M-1])