import sys
input = sys.stdin.readline

import copy
def wall(wall_cnt):
    # 벽 3개 설치시 함수실행
    if wall_cnt == 3:
        virus_start()
        return
    # 벽 설치 경우의 수 확인
    for n in range(N):
        for m in range(M):
            if graph[n][m] == 0:
                graph[n][m] = 1 # 벽 설치
                wall(wall_cnt + 1)
                graph[n][m] = 0 # dfs 실행 후 초기화

def virus_start():
    global answer
    # 기존 그래프 깊은 복사
    wall = copy.deepcopy(graph)
    virus = []
    # 바이러스 위치 담기
    for n in range(N):
        for m in range(M):
            if graph[n][m] == 2:
                virus.append((n,m))
    
    while virus:
        x, y = virus.pop()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and wall[nx][ny] == 0:
                wall[nx][ny] = 2
                virus.append((nx, ny))
    
    safezone_cnt = 0
    for row in wall:
        safezone_cnt += row.count(0) # 안전지대 카운트
    answer = max(answer, safezone_cnt)

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 0
    wall(0)
    print(answer)