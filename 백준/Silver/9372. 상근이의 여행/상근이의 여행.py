import sys
input = sys.stdin.readline
T = int(input()) # 테스트 케이스

for _ in range(T):
  N, M = map(int, input().split()) # 국가의 수 N, 비행기의 종류 M
  graph = [[] for i in range(N+1)]

  for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  visit = [0] * (N+1) # 방문 체크
  
  def DFS(idx, cnt):
    visit[idx] = 1 # 방문
    for i in graph[idx]:
      if visit[i] == 0:
        cnt = DFS(i, cnt+1)
    
    return cnt
  
  result = DFS(1, 0)
  print(result)