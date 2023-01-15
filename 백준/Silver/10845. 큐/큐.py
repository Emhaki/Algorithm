import sys
input = sys.stdin.readline
N = int(input())
result = []
for _ in range(N):
    a = input().split()
    if a[0] == "push":
        result.insert(0, a[1])

    elif a[0] == "front":
        if len(result) != 0:
            print(result[len(result) -1])
        else:
            print(-1)
    elif a[0] == "back":
        if len(result) != 0:
            print(result[0])
        else:
            print(-1)
    elif a[0] == "size":
        print(len(result))
    elif a[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "pop":
        if len(result) != 0:
            print(result.pop())
        else:
            print(-1)