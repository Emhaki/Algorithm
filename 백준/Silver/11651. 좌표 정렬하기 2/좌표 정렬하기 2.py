import sys
input = sys.stdin.readline

N = int(input())
result = []
for i in range(N):
    a, b = map(int, input().split())
    result.append((a, b))

k = sorted(result, key = lambda x: (x[1], x[0]))

for i in k:
    print(*i)