import sys
input = sys.stdin.readline

from itertools import combinations
N, M = map(int, input().split())
ch_list = []

for _ in range(N):
    ch_list.append(list(map(int, input().split())))
max_happy = 0

for a,b,c in combinations(range(M), 3):
    chicken = 0
    for i in range(N):
        chicken += max(ch_list[i][a], ch_list[i][b], ch_list[i][c])
    max_happy = max(chicken, max_happy)

print(max_happy)