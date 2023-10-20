import sys
N, M = map(int, sys.stdin.readline().split())
J = int(sys.stdin.readline())
now = 1
apples = []
answer = 0
for _ in range(J):
    apples.append(int(sys.stdin.readline()))
for apple in apples:
    if now <= apple and now + (M-1) >= apple:
        pass
    elif now > apple:
        answer += abs(apple - now)
        now = apple
    else:
        answer += apple - (M-1) - now
        now = apple - (M-1)
print(answer)