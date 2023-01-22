import sys
input = sys.stdin.readline

M = int(input())
result = set()

for _ in range(M):
    order = input().strip().split()

    if len(order) == 1:
        if order[0] == "all":
            result = set([i for i in range(1, 21)])
        elif order[0] == 'empty':
            result = set()
    else:
        a, b = order[0], order[1]
        b = int(b)

        if a == 'add':
            result.add(b)
        elif a == 'remove':
            result.discard(b)
        elif a == 'check':
            print(1 if b in result else 0)
        elif a == 'toggle':
            if b in result:
                result.discard(b)
            else:
                result.add(b)