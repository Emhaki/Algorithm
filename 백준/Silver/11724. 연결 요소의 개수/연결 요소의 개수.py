import sys
input = sys.stdin.readline
N, M = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
result = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)