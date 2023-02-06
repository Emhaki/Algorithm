import sys
input = sys.stdin.readline

graph = [list(map(str, input().split())) for _ in range(5)]
dx, dy = [0,0,-1,1], [-1,1,0,0]

def dfs(x,y, number):
    if len(number) == 6:
        if number not in result: # 중복을 제거하기 위해 if문
            result.append(number)
        return

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        else:
            dfs(nx, ny, number+graph[nx][ny]) # 문자열을 계속해서 더해줌

result = []
for i in range(5):
    for j in range(5):
        dfs(i,j, graph[i][j])
print(len(result))