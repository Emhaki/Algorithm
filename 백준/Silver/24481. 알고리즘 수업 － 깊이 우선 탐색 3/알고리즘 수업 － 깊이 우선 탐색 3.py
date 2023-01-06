import sys
input = sys.stdin.readline

from collections import deque

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
nodes_depth = [0 for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort(reverse=True)
stack = deque()
stack.append([r, 0])

while stack:
  node, depth = stack.pop()
  if visited[node]: continue
  visited[node] = True
  nodes_depth[node] = depth

  for next_node in graph[node]:
    if not visited[next_node]:
      stack.append([next_node, depth + 1])

for i in range(1, n+1):
  if i == r: print(0)
  elif nodes_depth[i] == 0: print(-1)
  else: print(nodes_depth[i])