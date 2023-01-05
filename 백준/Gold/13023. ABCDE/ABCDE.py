N, M = map(int, input().split())
rel = [[] for _ in range(N)]
visited = [0] * (N)
arrive = False

for _ in range(M):
  a, b = map(int, input().split())
  rel[a].append(b)
  rel[b].append(a)

def dfs(start, depth):
  global arrive
  visited[start] = 1
  if depth == 5:
    arrive = True
    return
  for nx in rel[start]:
    if visited[nx] == 0:
      dfs(nx, depth + 1)
  visited[start] = 0

for i in range(N):
  dfs(i, 1)
  if arrive:
    break

if arrive:
  print(1)
else:
  print(0)