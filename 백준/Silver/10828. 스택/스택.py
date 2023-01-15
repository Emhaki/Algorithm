import sys
input = sys.stdin.readline
N = int(input())
result = []

for _ in range(N):
    a = input().split()
    if a[0] == "push":
        result.append(a[1])
    elif a[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif a[0] == 'size':
        print(len(result))
    elif a[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])