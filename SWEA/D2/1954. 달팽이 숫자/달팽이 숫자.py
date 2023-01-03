T = int(input())

# row, col 인덱스 탐색 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(1, T+1):
  N = int(input())
  graph = [[0]*N for _ in range(N)]
  r, c = 0, 0
  
  direc = 0
  
  for n in range(1, N*N + 1):
    graph[r][c] = n
    r += dx[direc]
    c += dy[direc]

    if r < 0 or c < 0 or r >= N or c >= N or graph[r][c] != 0:
      # 실행취소
      r -= dx[direc]
      c -= dy[direc]

      direc = (direc + 1) % 4

      r += dx[direc]
      c += dy[direc]

  print(f'#{_}')
  for row in graph:
    print(*row)