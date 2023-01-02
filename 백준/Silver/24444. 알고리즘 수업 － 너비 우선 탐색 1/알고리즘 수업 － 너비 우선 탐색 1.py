from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(r):
  global count

  Q = deque([r])
  visited[r] = 1
  while Q:
    r = Q.popleft()
    graph[r].sort()
    for nx in graph[r]:
      if visited[nx] == 0:
        count += 1
        visited[nx] = count
        Q.append(nx)

bfs(r)
for v in visited[1:]:
  print(v)