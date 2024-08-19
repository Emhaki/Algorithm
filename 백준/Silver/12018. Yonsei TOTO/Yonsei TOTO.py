import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

for _ in range(n):
    p, l = map(int, input().split())
    l_list = list(map(int, input().split()))
    l_list.sort(reverse=True)

    if p < l:
        result.append(1)
    else:
        result.append(l_list[l-1])

result.sort()
count = 0

for i in result:
    if m-i >= 0:
        m -= i
        count += 1
    else:
        break

print(count)