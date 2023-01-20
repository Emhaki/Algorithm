from collections import deque
# N 세로길이
# M 가로길이
# K 음식물 쓰레기 개수
N, M, K = map(int, input().split())
graph = [[]]
for i in range(N+1):
    graph.append([0] * (M+1))
for i in range(K):
    a, b = map(int, input().split())
    graph[a][b] = 1
#[
# [], 
# [1, 0, 0, 0], 
# [0, 1, 1, 0], 
# [1, 1, 0, 0]
# ]

# 4방향 탐색
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i, j, graph):
    q = deque([[i, j]])
    graph[i][j] = 2
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= N and 0 < ny <= M and graph[nx][ny] == 1: # 방향을 탐색하면서 범위 설정 및 쓰레기인지
                q.append([nx, ny]) # 범위도 맞고 쓰레기도 맞다면 좌표 append
                graph[nx][ny] = 2 # 방문처리
                cnt += 1
    return cnt

answer = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i][j] == 1:
            ans = bfs(i, j, graph)
            answer = max(ans, answer)
print(answer)