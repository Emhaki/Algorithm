import sys
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
graph = [list(map(str, input().strip())) for _ in range(N)]
dx, dy = [0,0,-1,1], [-1,1,0,0]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    hearts_x, hearts_y = 0, 0

    while queue:
        x, y = queue.popleft()
        heart = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == "*":
                    heart += 1
                    if heart == 4:
                        hearts_x, hearts_y = x, y   
                        return hearts_x + 1, hearts_y + 1

left_arm = 0
right_arm = 0
head = 0
weight = 0
left_leg = 0
right_leg = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == '*':
            if bfs(i,j):
                hearts_x, hearts_y = bfs(i,j)
                
# 심장을 중심으로 왼팔
for i in range(hearts_y - 1):
    if graph[hearts_x-1][i] == "*":
        left_arm += 1
        
# 심장을 중심으로 오른팔
for i in range(hearts_y, N):
    if graph[hearts_x-1][i] == "*":
        right_arm += 1

weight_end = 0
# 심장을 중심으로 아래
for i in range(hearts_x, N):
    if graph[i][hearts_y-1] == "*":
        weight += 1
        weight_end = i
        
# 허리끝을 중심으로 왼쪽다리
for i in range(weight_end+1, N):
    if graph[i][hearts_y-2] == "*":
        left_leg += 1

# 허리끝을 중심으로 오른쪽다리
for i in range(weight_end+1, N):
    if graph[i][hearts_y] == "*":
        right_leg += 1

print(hearts_x, hearts_y)
print(left_arm, right_arm, weight, left_leg, right_leg)