import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N, M, R = map(int, input().strip().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
cnt = 1

for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(len(graph)):
  graph[i].sort(reverse=True)

def dfs(R):
  global cnt
  visited[R] = cnt
  for nx in graph[R]:
    if visited[nx] == 0:
      cnt += 1 
      visited[nx] = cnt
      dfs(nx)

dfs(R)
for i in visited[1:]:
  print(i)