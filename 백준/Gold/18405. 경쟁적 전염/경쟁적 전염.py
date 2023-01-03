import sys
input = sys.stdin.readline

from collections import deque

# 크기 및 바이러스 종류
n, k = map(int, input().split())

# 바이러스 정보 저장
graph = []
# 바이러스의 추가 정보 저장
data = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  # 바이러스의 추가 정보 저장
  for j in range(n):
    # 해당 위치에 바이러스가 존재하는 경우 (0이 아니라면 바이러스)
    if graph[i][j] != 0:
      # 바이러스 정보저장 (바이러스 종류, 확산 시간, x축 위치, y축 위치)
      data.append((graph[i][j], 0, i, j))

# 바이러스를 번호가 낮은 순서대로 정렬
data.sort()
# 바이러스 추가 정보를 큐로 변환
q = deque(data)

# s초와 (x,y)에 존재하는 바이러스의 종류
s, x, y = map(int, input().split())

# 상하좌우 이동 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
  
  # q의 첫번째 원소를 각각에 할당
  virus, time, i, j = q.popleft()

  # 현재 위치의 바이러스가 S초까지 확산된 바이러스라면 종료
  if time == s:
    break

  # 상하좌우 계산
  for m in range(4):
    nx = i + dx[m]
    ny = j + dy[m]
    # 범위 설정
    if (0 <= nx and nx < n and 0 <= ny and ny < n and graph[nx][ny] == 0):
      # 그래프에 바이러스 확산 표시
      graph[nx][ny] = virus
      # 큐에 삽입 (시간 +1)
      q.append((virus, time+1, nx, ny))

print(graph[x-1][y-1])