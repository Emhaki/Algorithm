import sys
input = sys.stdin.readline
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
    graph[r].sort(reverse=True) # 그래프 정렬
    for nx in graph[r]:
      if visited[nx] == 0: # 방문하지 않았을 경우
        count += 1
        visited[nx] = count # 방문 순서 카운트
        Q.append(nx)

bfs(r)
for v in visited[1:]: # 인덱스 1부터
  print(v)