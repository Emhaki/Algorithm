from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_ = [list(map(str, input().strip())) for _ in range(N)]

dx, dy = [0,0,-1,1], [-1,1,0,0]


def bfs(i,j):
    queue = deque([(i,j)])
    people = 0

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < M and list_[nx][ny] != "X":
                if list_[nx][ny] == "P":
                    people += 1
                list_[nx][ny] = "X"
                queue.append((nx, ny))
                
    return ["TT", people] [people > 0]
sx, sy = 0, 0

for i in range(N):
    for j in range(M):
        if list_[i][j] == "I":
            sx, sy = i, j
            list_[i][j] = "X" 

print(bfs(sx,sy))