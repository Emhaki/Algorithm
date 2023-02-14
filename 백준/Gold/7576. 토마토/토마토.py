import sys
input = sys.stdin.readline

from collections import deque
M, N = map(int, input().split())

boxes = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0,0,-1,1], [-1,1,0,0]
queue = deque()
def bfs():
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < M and boxes[nx][ny] == 0:
                boxes[nx][ny] = boxes[x][y] + 1 
                queue.append((nx,ny))

answer = 0
for i in range(N):
    for j in range(M):
        if boxes[i][j] == 1:
            queue.append((i,j))

bfs()
for line in boxes:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(line))

print(answer - 1)