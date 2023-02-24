import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def dfs(n):
    for i in graph[n]:
        if visited[i] == 0:
            visited[i] = n
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])