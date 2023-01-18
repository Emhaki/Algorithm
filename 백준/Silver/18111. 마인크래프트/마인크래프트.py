import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
result = sys.maxsize # 최댓값 설정

# 0층부터 256층까지 반복
for target in range(257):
    max_time, min_time = 0, 0
    # graph = [
    #          [0, 0, 0, 0], 
    #          [0, 0, 0, 0], 
    #          [0, 0, 0, 1]
    #         ]

    # 반복문을 통해 블록을 확인
    for i in range(N):
        for j in range(M):
            
            # 블록이 층수보다 더 크다면 max_time에 기록
            if graph[i][j] >= target:
                max_time += graph[i][j] - target
            
            # 블록이 층수보다 더 작으면 min_time에 기록
            else:
                min_time += target - graph[i][j]

    if max_time + B >= min_time:
        # 시간 초를 구하고 최저 시간과 비교
        if min_time + (max_time * 2) <= result:
            result = min_time + (max_time * 2) # 최저 시간
            floor = target # 층수

print(result, floor)