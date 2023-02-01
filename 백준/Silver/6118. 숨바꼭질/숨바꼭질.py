import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 연결

visited = [0] * (N+1)

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        start = queue.popleft()
        
        for i in graph[start]:
            if visited[i] == 0: # 방문하지 않은 곳이라면
                visited[i] = visited[start] + 1
                queue.append(i)

bfs(1)
max_num = max(visited)

print(visited.index(max_num), max_num - 1, visited.count(max_num))