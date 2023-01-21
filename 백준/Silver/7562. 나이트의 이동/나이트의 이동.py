import sys
input = sys.stdin.readline


# 0 0 현재 있는 칸
# 7 0 가려하는 칸
from collections import deque


dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(y, x, gr, gc):
    queue = deque()
    queue.append([y, x])
    visited[y][x] = 1

    while queue:
        r, c = queue.popleft()

        if r == gr and c == gc: # 방문하고자 하는 곳이면
            print(visited[r][c] - 1)
            return

        for i in range(8):
            rx = r + dr[i]
            ry = c + dc[i]

            if 0 <= rx < L and 0 <= ry < L and not visited[rx][ry]:
                queue.append([rx, ry])
                visited[rx][ry] = visited[r][c] + 1

T = int(input())
for _ in range(T):
    L = int(input())
    nr, nc = map(int, input().split())
    gr, gc = map(int, input().split())

    if nr == gr and nc == gc:
        print(0)
        continue
    visited = [[False] * L for _ in range(L)]
    bfs(nr, nc, gr, gc)
