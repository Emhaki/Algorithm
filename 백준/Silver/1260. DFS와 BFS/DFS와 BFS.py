from collections import deque
N, M, V = map(int, input().split())

graph = [[] for i in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  graph[a].sort()
  graph[b].sort()

# DFS함수
def dfs(graph, V, visited):
  visited[V] = 1
  print(V, end=' ')
  for nx in graph[V]:
    if visited[nx] == 0:
      dfs(graph, nx, visited)

# BFS함수
def bfs(graph, V, visited):
  Q = deque([V])
  visited[V] = 1
  while Q:
    C = Q.popleft()
    print(C, end=' ')
    for nx in graph[C]:
      if visited[nx] == 0:
        Q.append(nx)
        visited[nx] = 1

visited = [0] * (N+1)
dfs(graph, V, visited)
print("")
visited = [0] * (N+1)
bfs(graph, V, visited)