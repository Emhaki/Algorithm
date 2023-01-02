def dfs_horizontal(x,y):

  # 주어진 범위를 벗어나는 경우에 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == '-':

    # 해당 노드 방문 처리
    graph[x][y] = 'o'

    # 좌, 우의 위치들도 모두 재귀적으로 호출
    dfs_horizontal(x, y - 1)
    dfs_horizontal(x, y + 1)

    return True
  return False

def dfs_vertical(x, y):

  # 주어진 범위를 벗어나는 경우에 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == '|':

    graph[x][y] = 'o'

    # 상, 하의 위치들도 모두 재귀적으로 호출
    dfs_vertical(x - 1, y)
    dfs_vertical(x + 1, y)

    return True
  return False

n, m = map(int, input().split())

graph = [list(input()) for _ in range(n)]

cnt = 0
# n 세로, m 가로
for i in range(n):
  for j in range(m):
    if graph[i][j] == '-':
      dfs_horizontal(i, j)
      cnt += 1
    elif graph[i][j] == '|':
      dfs_vertical(i, j)
      cnt += 1

print(cnt)