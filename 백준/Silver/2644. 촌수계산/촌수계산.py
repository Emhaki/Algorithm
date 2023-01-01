n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

def dfs(a):
  for nx in graph[a]:
    if visited[nx] == 0:
      visited[nx] = visited[a]+1
      dfs(nx)

dfs(a)
print(visited[b] if visited[b] > 0 else -1)