from collections import deque


n = int(input())
# 1 ~ 입력값을 queue에 할당
# queue = deque([1, 2, 3, 4, 5, 6, 7])
queue = deque(range(1, n+1))
# queue가 1보다 크다면 계속 반복
while len(queue) > 1:
    # queue 버린 값들을 출력
    print(queue.popleft(), end=" ")
    # queue에 버리고 난 후 맨 위에 카드를 새롭게 추가
    queue.append(queue.popleft())

# 남아있는 카드를 출력
print(queue[0])