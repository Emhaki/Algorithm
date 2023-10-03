from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(N)]

    while queue:
        q = queue.popleft()

        for i in range(N):
            if check[i] == 0 and graph[i][q] == 1:
                queue.append(i)
                check[i] = 1
                visited[i][x] = 1

for i in range(N):
    bfs(i)

for i in visited:
    print(*i)