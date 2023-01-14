N = int(input())
list_ = []
for i in range(N):
    a, b = map(int, input().split())
    list_.append((a, b))
result = sorted(list_, key = lambda x : (x[0], x[1]))
for i in result:
    print(*i)   