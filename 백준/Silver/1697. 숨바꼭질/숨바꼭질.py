import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().split())
MAX = 100001
visited = [-1] * MAX
visited[N] = 0 # 수빈이의 위치 방문처리
queue = deque()
queue.append((N,N))

# 수빈이가 더 큰 곳에 있다면 곱하기 연산과 더하기 연산은 불필요
if N > K: # K = 5, N = 17
    print(N - K)

else:
    while queue:
        x, move = queue.popleft()

        if x == K:
            print(visited[x])
            break
        
        for j in (x - 1), (x + 1), (x * 2):
            if 0 <= j < MAX and visited[j] == -1:
                visited[j] = visited[x] + 1 # 시간 기록
                queue.append((j, move + j))