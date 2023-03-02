import sys
input = sys.stdin.readline

from collections import deque
N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)

    while queue:
        nx = queue.popleft()
        print(nx, end=' ')

        for i in graph[nx]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

def dfs(v):
    visited[v] = 1
    print(v, end=' ')

    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)


visited = [0] * (N+1)
dfs(V)
print('')
visited = [0] * (N+1)
bfs(V)