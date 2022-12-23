N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [0]*(N+1) # 사람이 읽기 쉽게 1, 2, 3으로
# 그래프 생성
for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a) # 양방향 연결
# 함수 DFS
def dfs(M): #연결선의 갯수
  visited[M] = 1
  for nx in graph[M]:
    if visited[nx] == 0:
      dfs(nx)

dfs(1)
print(sum(visited)-1)