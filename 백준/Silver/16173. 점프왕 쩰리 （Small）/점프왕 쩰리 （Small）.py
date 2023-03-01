import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def dfs(x,y):
    
    if x <= -1 or x >= N or y <= -1 or y >= N or visited[x][y] == True:
        return
    
    if board[x][y] == -1:
        visited[x][y] = 1
        return
    
    visited[x][y] = 1

    dfs(x+board[x][y], y)
    dfs(x,y+board[x][y])

dfs(0,0)

if visited[-1][-1] == True:
    print('HaruHaru')
elif visited[-1][-1] == False:
    print('Hing')