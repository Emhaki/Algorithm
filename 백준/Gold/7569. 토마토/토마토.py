import sys
input = sys.stdin.readline

from collections import deque

move = [(0,0,1), (0,0,-1), (1,0,0), (0,1,0), (-1,0,0), (0,-1,0)]
M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)] # 3차원
queue = deque()


for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                  queue.append((i,j,k))

while queue:
    i, j, k = queue.popleft()
    
    for di, dj, dk in move:
        ni = di + i
        nj = dj + j
        nk = dk + k

        if ni < 0 or ni >= H or nj < 0 or nj >= N or nk < 0 or nk >= M:
            continue
        if graph[ni][nj][nk] == -1:
            continue
        if not graph[ni][nj][nk]:
            graph[ni][nj][nk] = graph[i][j][k] + 1 # 시간체크
            queue.append((ni, nj, nk))
            
answer = 0
# [[[5, 4, 3, 4, 5], [4, 3, 2, 3, 4], [5, 4, 3, 4, 5]], [[4, 3, 2, 3, 4], [3, 2, 1, 2, 3], [4, 3, 2, 3, 4]]]
for floor in graph:
    for i in range(len(floor)):
        answer = max(max(floor[i]) - 1, answer)

for floor in graph:
    for row in floor:
        if 0 in row:
            answer = -1

print(answer)