import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 첫째 줄에 N과 고속도로의 길이 D
INF = sys.maxsize
N, D = map(int, input().split())
road = [[] for _ in range(D+1)]
visited = [INF] * (D+1)

def dijkstar(start):
    queue = []
    heappush(queue, (0, start)) # 시작 노드부터 탐색 시작
    visited[start] = 0 # 시작노드까지 거리는 0

    while queue:
        distance, now = heappop(queue) # 탐색할 노드와 거리리

        if distance > visited[now]: # 기존 최단거리보다 멀다면 무시
            continue
        
        for i in road[now]: # [0, 50, 10]
            cost = distance + i[1] # 인접노드까지의 거리
            if cost < visited[i[0]]: # 기존값보다 작다면
                visited[i[0]] = cost # 최소값 저장
                heappush(queue,(cost, i[0]))

# 거리를 1로 초기화
for i in range(D):
    road[i].append((i+1, 1))

for _ in range(N):
    start, end, fast = map(int, input().split())

    if end > D: # 고속도로 길이보다 끝이 더 길다면
        continue
    road[start].append((end,fast))

dijkstar(0)
print(visited[D])