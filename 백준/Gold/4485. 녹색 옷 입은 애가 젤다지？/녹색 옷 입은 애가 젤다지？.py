import sys
input = sys.stdin.readline

from heapq import heappop, heappush
INF = sys.maxsize
dx = [0,0,-1,1]
dy = [-1,1,0,0]
case_cnt = 0

while True:
    case_cnt +=1
    N = int(input())

    # 0을 입력받으면 반복문 탈출
    if N == 0: break

    # 최솟값을 찾기위해 Max값으로 2차원 리스트 형성
    distance = [[INF] * N for _ in range(N)]
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 시작지점
    distance[0][0] = graph[0][0]
    
    queue = []
    heappush(queue, (graph[0][0], 0, 0))

    while queue:
        
        # move에는 graph[x][y]까지의 최단 경로 저장
        # x, y 는 탐색을 시작하는 좌표
        move, x, y = heappop(queue)

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            # 비용을 기록
            cost = move + graph[nx][ny]
            
            # distance[nx][ny]가 비용보다 크다면 그 위치에 비용을 기록
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                heappush(queue, (cost, nx, ny))

    print(f"Problem {case_cnt}: {distance[N-1][N-1]}")