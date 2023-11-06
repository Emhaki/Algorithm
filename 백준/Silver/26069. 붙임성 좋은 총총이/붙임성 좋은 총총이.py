import sys
input = sys.stdin.readline

N = int(input())
dance = {'ChongChong'}
for i in range(N):
    a, b = input().strip().split()
    
    if a in dance:
        dance.add(b)
    if b in dance:
        dance.add(a)

print(len(dance))