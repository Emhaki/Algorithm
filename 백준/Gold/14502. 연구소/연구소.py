import sys
input = sys.stdin.readline
from itertools import combinations
import copy

def solve():
    global answer

    for wall_combi in combinations(empty, wall_num):
        graph_new = copy.deepcopy(graph)
        for x, y in wall_combi:
            graph_new[x][y] = 1
        
        # 바이러스 위치
        virus = []
        for n in range(N):
            for m in range(M):
                if graph_new[n][m] == 2:
                    virus.append((n,m))
        
        while virus:
            xv, yv = virus.pop()
            
            for i in range(4):
                nx = dx[i] + xv
                ny = dy[i] + yv

                if 0 <= nx < N and 0 <= ny < M and graph_new[nx][ny] == 0:
                    graph_new[nx][ny] = 2
                    virus.append((nx,ny))
        
        safe_zone_cnt = 0
        for row in graph_new:
            safe_zone_cnt += row.count(0)
        answer = max(answer, safe_zone_cnt)

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
empty = []
for n in range(N):
    for m in range(M):
        if graph[n][m] == 0:
            empty.append((n,m))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
answer = 0
wall_num = 3
solve()
print(answer)