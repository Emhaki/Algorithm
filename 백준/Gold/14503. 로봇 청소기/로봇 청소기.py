import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 방의 크기
r, c, d = map(int, input().split()) # 로봇의 위치와 방향

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 시작 지점 카운트
visited[r][c] = 1
cnt = 1

while True:
    clean = 0
    for _ in range(4):
        d = (d+3) % 4 # 왼쪽방향으로 한 칸 돌린다.
        nx = dx[d] + r
        ny = dy[d] + c

        # 범위 내에 있고, 빈 칸이고, 청소할 수 있다면
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny] == 0:
            visited[nx][ny] = 1 # 방문처리
            cnt += 1
            r = nx
            c = ny
            clean = 1 # 청소를 했음
            break

    if clean == 0: 
        if graph[r - dx[d]][c - dy[d]] == 1: # 후진했을 때 벽이라면 break
            print(cnt)
            break
        else:
            r, c = r - dx[d], c - dy[d]