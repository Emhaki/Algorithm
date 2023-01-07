import sys
input = sys.stdin.readline

from collections import deque
n, m, r = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False for _ in range(n+1)]
nodes_depth = [0 for _ in range(n+1)]
nodes_cnt = [0 for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(n+1):
  graph[i].sort(reverse=True)

stack = deque()
stack.append([r, 0])
cnt = 1

while stack:
  current, depth = stack.pop()
  if visited[current]: continue
  visited[current] = True
  nodes_depth[current] = depth
  nodes_cnt[current] = cnt
  cnt += 1
  for nx in graph[current]:
    if not visited[nx]:
      stack.append([nx, depth + 1])
  
result = 0
for i in range(1, n+1):
  if i == r or nodes_depth[i] == 0: continue
  else: result += nodes_depth[i]*nodes_cnt[i]

print(result)