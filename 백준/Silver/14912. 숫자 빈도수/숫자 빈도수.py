import sys
input = sys.stdin.readline

N, number = map(int, input().split(" "))
count = 0
for i in range(1, N+1):
    for j in str(i):
        if int(j) == number:
            count += 1
print(count)