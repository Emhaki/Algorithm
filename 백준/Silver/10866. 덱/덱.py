import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
result = []
result = deque()
for _ in range(N):
    a = input().split()
    if a[0] == "push_front":
        result.appendleft(a[1])
    elif a[0] == "push_back":
        result.append(a[1])
    elif a[0] == "pop_front":
        if len(result) == 0:
            print(-1)
        else:
            print(result.popleft())
    elif a[0] == "pop_back":
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif a[0] == "size":
        print(len(result))
    elif a[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(result) == 0:
            print(-1)
        else:
            print(result[0])
    elif a[0] == "back":
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])