import sys
input = sys.stdin.readline

# 수빈이는 걷거나 순간이동을 할 수 있다. 
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동의 경우 1초 후에 2*X의 위치로 이동하게 된다.

from collections import deque
# 수빈이가 N, 동생이 K
N, K = map(int, input().split())
# 수빈이가 방문할 때 걸리는 시간을 나타내느 정보
visited = [0] * 100001
# 수빈이가 동생을 만나기 전에 어떤 좌표를 이동했는지 표시하는 정보
check = [0] * 100001

def move(current):
    
    location = []
    temp = current

    for _ in range(visited[current]+1):
        # 위치 추가
        location.append(temp)
        # 전의 위치 받기
        temp = check[temp]
    
    # 거꾸로 출력
    print(' '.join(map(str, location[::-1])))

# 너비 우선 탐색 진행
def bfs():
    queue = deque()
    
    # 수빈이 위치 넣기
    queue.append(N)

    while queue:
        current = queue.popleft()
        # 수빈이가 동생을 만난다면
        if current == K:
            # 걸린 시간 출력
            print(visited[current])
            move(current)
            return
        
        # 조건에 해당하는 방식을 모두 탐색
        for next_step in (current-1, current+1, current*2):
            # 다음 이동할 위치가 이동가능한 좌표이며 아직 방문하지 않았다면
            if 0 <= next_step <= 100000 and visited[next_step] == 0:
                visited[next_step] = visited[current] + 1
                queue.append(next_step)
                # 수빈이가 지나온 위치를 알기위해 다음 이동위치에 현재 이동위치 기록
                check[next_step] = current

bfs()