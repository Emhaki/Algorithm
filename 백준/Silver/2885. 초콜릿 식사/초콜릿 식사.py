import sys
input = sys.stdin.readline

N = int(input())

size = 1
# 자른 횟수
cut = 0
# size가 N보다 클때까지 제곱
while size < N:
    size *= 2

temp = size

while N > 0:
    if N >= size:
        N -= size
    else:
        size //= 2
        cut += 1

print(temp, cut)