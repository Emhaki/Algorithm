import sys
input = sys.stdin.readline

from collections import deque
N = int(input())
num = int(input())
num_list = [[] for _ in range(N+1)]
for _ in range(num):
    a, b = map(int, input().split())
    num_list[a].append(b)
    num_list[b].append(a)

visited = [0 for _ in range(N+1)]

def bfs(x):
    queue = deque()
    visited[x] = 1
    queue.append(x)

    while queue:
        nx = queue.popleft()

        for i in num_list[nx]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[nx] + 1

bfs(1)
result = 0
for i in range(2, N+1):
    if visited[i] < 4 and visited[i] != 0:
        result += 1
        
print(result)