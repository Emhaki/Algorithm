import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))

load = [int(input()) for i in range(N)]
now = 0

for i in range(1, N):
    now += int(input())

    if now >= N-1:
        print(i)
        break

    now += load[now]

    if now >= N-1:
        print(i)
        break