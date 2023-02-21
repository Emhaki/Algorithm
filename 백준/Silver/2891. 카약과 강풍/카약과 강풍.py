import sys
input = sys.stdin.readline
N, S, R = map(int, input().split())

team = list(map(int, input().split()))
angel = list(map(int, input().split()))

count = S

for i in angel:
    if i in team:
        team.remove(i)
        angel.remove(i)
        count -= 1

for i in team:
    for j in angel:
        if j - 1 <= i <= j + 1:
            angel.remove(j)
            count -= 1
            break
        elif j + 1 < i:
            break

print(count)