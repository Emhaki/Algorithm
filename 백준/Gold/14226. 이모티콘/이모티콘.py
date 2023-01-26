from collections import deque
S = int(input())

visited = [[-1] * (S + 1) for _ in range(S + 1)]
queue = deque()
queue.append((1,0))
visited[1][0] = 0
# S가 2일때
# [
# [-1, -1, -1], [0, -1, -1], [-1, -1, -1]
# ]

# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
# 3. 화면에 있는 이모티콘 중 하나를 삭제

while queue:
    screen, clip = queue.popleft()

    if S == screen:
        print(visited[screen][clip])
        break
    
    if visited[screen][screen] == -1:
        visited[screen][screen] = visited[screen][clip] + 1
        queue.append((screen, screen))
    
    if screen + clip <= S and visited[screen + clip][clip] == -1:
        visited[screen + clip][clip] = visited[screen][clip] + 1
        queue.append((screen + clip, clip))
    
    if screen - 1 >= 0 and visited[screen - 1][clip] == -1:
        visited[screen - 1][clip] = visited[screen][clip] + 1
        queue.append((screen - 1, clip))