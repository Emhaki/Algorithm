import sys
input = sys.stdin.readline

from collections import deque
import copy

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def Cheese():
    global cheddar
    melting = copy.deepcopy(cheddar)
    cheddar = deque()

    while melting:
        x, y = melting.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and ((not visited[nx][ny] and not graph[nx][ny]) or graph[nx][ny] == 1):
                visited[nx][ny] += 1
                if graph[nx][ny] == 1:
                    if visited[nx][ny] >= 2:
                        cheddar.append((nx, ny))
                    
                if graph[nx][ny] == 0:
                    melting.append((nx,ny))
    
    # 치즈 삭제
    for x, y in cheddar:
        graph[x][y] = 0 


cheddar = deque([(0,0)])
cnt = 0

while cheddar:
    Cheese()

    if cheddar:
        cnt += 1

print(cnt)