import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)
T = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x, y):

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
            graph[ny][nx] = 0
            dfs(nx,ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for i in range(N)]
    cnt = 0

    for i in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x,y)
                cnt += 1

    print(cnt)