import sys
input = sys.stdin.readline
from itertools import permutations
N, K = map(int, input().split())
day = list(map(int, input().split()))

answer = 0
for i in permutations(day, N):
    muscle = 500
    cnt = 0
    for j in i:
        muscle += j # 운동키트 증가량
        muscle -= K # k만큼 빠짐
        if muscle >= 500:
            cnt += 1

    if cnt == N:
        answer += 1

print(answer)