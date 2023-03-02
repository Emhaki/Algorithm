import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

house_list = []

def dfs(x,y):
    visited[x][y] = 1 # 방문처리
    global house_cnt
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and graph[nx][ny] == 1:
            dfs(nx,ny)
            house_cnt += 1

house_cnt = 1
cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and graph[i][j] == 1:
            dfs(i,j)
            house_list.append(house_cnt)
            house_cnt = 1
            cnt += 1

print(cnt)
house_list.sort()
for i in house_list:
    print(i)