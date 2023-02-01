import sys
input = sys.stdin.readline

from collections import deque

# S가 고슴도치
# D가 동굴
# * 물덩이
R, C = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 물이 차있는 지역 bfs
def water_bfs():
    global water
    water_local = deque()

    while water:
        x, y = water.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            # 이동할 수 있는 곳이라면
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                graph[nx][ny] = 'X' # 그래프 변경
                visited[nx][ny] = 1 # 방문처리
                water_local.append((nx,ny))
    
    # 물이 찰 수 있는 지역이 다 채워졌다면 
    for a, b in water_local:
        water.append((a,b))

def dochi_bfs():
    global queue

    while queue:
        dochi_queue = []
        
        while queue:
            x, y = queue.popleft()
            
            # 물과 돌이 아니라면
            if graph[x][y] != 'X' and graph[x][y] != '*':
                
                for i in range(4):
                    nx = dx[i] + x
                    ny = dy[i] + y

                    if 0 <= nx < R and 0 <= ny < C:
                        
                        # 고슴도치의 굴이라면 굴까지 걸리는 이동 횟수 리턴
                        if graph[nx][ny] == 'D':
                            return visited[x][y] + 1
                        
                        # 비어있는 곳이고 탐색하지 않은 곳이라면 탐색
                        elif graph[nx][ny] == '.' and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1 # 탐색 시간 추가
                            dochi_queue.append((nx, ny))

        # 고슴도치가 이동할 수 있는 곳을 모두 이동했다면                    
        for a, b in dochi_queue:
            queue.append((a,b))
        
        # water_bfs 실행
        water_bfs()
    
    return 'KAKTUS'

queue = deque()
water = deque()

result = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            queue.append((i,j))
        
        elif graph[i][j] == '*':
            water.append((i,j))
        
print(dochi_bfs())