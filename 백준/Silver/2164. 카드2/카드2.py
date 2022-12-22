from collections import deque
N = int(input())
list_ = [i+1 for i in range(N)]
list_ = deque(list_)
for i in range(len(list_)-1):
  list_.popleft() # 왼쪽 제거
  list_.rotate(-1) # 맨 뒤로 보내기
print(*list_)