from itertools import combinations
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

house = [] # 집 좌표
chicken = [] # 치킨집 좌표

for r in range(N): # x
  for c in range(N): # y
    if graph[r][c] == 1: house.append([r,c]) # [[0, 2], [1, 4], [2, 1], [3, 2]]
    elif graph[r][c] == 2: chicken.append([r,c]) # [[1, 2], [2, 2], [4, 4]]

result = 1e9 # 1000000000.0
for x in combinations(chicken, M): # 치킨집 좌표 리스트를 기준으로 M개 조합 ([1, 2], [2, 2], [4, 4])
  graph_dist = 0
  for h in house: # 전체 집 순회
    house_dist = 1e9
    for k in x: # 집별로 치킨집 순회
      house_dist = min(house_dist, abs(h[0]-k[0]) + abs(h[1]-k[1])) # 집별로 가장 가까운 치킨집 거리
    graph_dist += house_dist # 도시 치킨 거리 += 집에서 가장 가까운 치킨집 거리
  result = min(result, graph_dist)

print(result)