from collections import deque

F, S, G, U, D = map(int, input().split())

def bfs(start):
    q = deque([start])

    cnt = [-1] * F # 방문하지 않은 층수를 1로 설정
    cnt[start] = 0 # 방문한 곳 방문처리

    while q:
        cur_floor = q.popleft()
        if cur_floor == G - 1:
            return cnt[cur_floor]
        
        for i in range(2):
            if i == 0:
                next_floor = cur_floor + U
            else:
                next_floor = cur_floor - D
            
            if not 0 <= next_floor < F or cnt[next_floor] != -1: # 범위, 방문 여부
                continue

            q.append(next_floor)
            cnt[next_floor] = cnt[cur_floor] + 1
    return 'use the stairs'

print(bfs(S - 1))