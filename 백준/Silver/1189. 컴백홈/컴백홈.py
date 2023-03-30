import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
graph = [list(map(str, input().strip())) for _ in range(R)]
answer = 0
# [
# ['.', '.', '.', '.'],
# ['.', 'T', '.', '.'],
# ['.', '.', '.', '.']
# ]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x, y, cnt):
    global answer

    if cnt == K and x == 0 and y == C - 1:
        answer += 1
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
            graph[nx][ny] = 'T'
            dfs(nx, ny, cnt+1)
            graph[nx][ny] = '.'

graph[R-1][0] = 'T' # 왼쪽 아래 스타트
dfs(R-1,0,1) # 왼쪽 아래 스타트
print(answer)