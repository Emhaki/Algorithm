import sys
input = sys.stdin.readline

INF = sys.maxsize
N = int(input())
team = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * (N+1)
result = INF

def solve(depth, idx):
    global result
    if depth == (N//2):
        start, link = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if visited[i] and visited[j]: # 둘 다 방문했다면
                    start += (team[i][j] + team[j][i]) # 방문한 사람은 스타트팀에
                elif not visited[i] and not visited[j]:
                    link += (team[i][j] + team[j][i]) # 방문안한 사람은 링크팀에

        result = min(result, abs(start - link)) # 최솟값을 갱신
    
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            solve(depth+1, i+1)
            visited[i] = False

solve(0, 0)
print(result)