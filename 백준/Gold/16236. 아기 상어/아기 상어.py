import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

baby_shark = []

# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있은 물고기라 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

dx = [0,0,-1,1]
dy = [-1,1,0,0]

shark_size = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            baby_shark.append((i,j))

#  아기 상어 위치
x, y = baby_shark.pop()

def bfs(i,j, shark_size):
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값
    queue = deque()
    queue.append((i,j))

    visited[i][j] = 1
    temp = []

    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx = dx[i] + xx
            ny = dy[i] + yy

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:

                if graph[nx][ny] <= shark_size:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1 # 방문처리
                    distance[nx][ny] = distance[xx][yy] + 1 # 거리 증가
                    
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        temp.append((nx,ny, distance[nx][ny]))
    
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그런 물고기가 여러마리라면, 가잔 왼쪽에 있는 물고기를 먹는다.
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))

cnt = 0
result = 0

while True:
    shark = bfs(x,y,shark_size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 브레이크
    if len(shark) == 0:
        break

    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그런 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # 정렬한 결과를 반영    
    nx, ny, dist = shark.pop()

    # 움직이는 거리 합산
    result += dist
    graph[x][y] , graph[nx][ny] = 0,0

    # 상어좌표를 옮겨준다.
    x, y = nx, ny
    cnt += 1

    if cnt == shark_size:
        shark_size += 1
        cnt = 0

print(result)