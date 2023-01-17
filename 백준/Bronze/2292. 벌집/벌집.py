import sys
input = sys.stdin.readline
N = int(input())

bee_house = 1
cnt = 1
# [1, 6, 12, 13, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78]
while N > bee_house:
    bee_house += 6 * cnt
    cnt += 1
print(cnt)