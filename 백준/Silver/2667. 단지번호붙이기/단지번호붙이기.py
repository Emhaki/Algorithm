import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[-1]* N for _ in range(N)]
dx, dy = [0,0,-1,1], [-1,1,0,0]
queue = deque()
answer = []
def bfs(i,j):
    queue.append((i,j))
    visited[i][j] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == -1:
                graph[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))
    return cnt
                





for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            answer.append(bfs(i,j))
            
        
answer.sort()
print(len(answer))
for i in answer:
    print(i)