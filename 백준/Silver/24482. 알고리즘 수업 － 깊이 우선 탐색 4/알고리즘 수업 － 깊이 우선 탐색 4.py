import sys
input = sys.stdin.readline
from collections import deque

n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [0 for _ in range(n+1)]
nodes_depth = [0 for _ in range(n+1)]

for _ in range(m): # 간선의 갯수
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(len(graph)):
  graph[i].sort()

stack = deque()
stack.append([r, 0])

while stack:
  c, depth = stack.pop()
  if visited[c]:
    continue
  visited[c] = 1
  nodes_depth[c] = depth

  for nx in graph[c]:
    if visited[nx] == 0:
      stack.append([nx, depth + 1])

for i in range(1, n+1):
  if i == r:
    print(0)
  elif nodes_depth[i] == 0:
    print(-1)
  else:
    print(nodes_depth[i])