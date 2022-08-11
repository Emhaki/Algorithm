A, B, C = map(int, input().split())

arr = [0]*100
answer = 0
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        arr[i] += 1

for j in arr:
    answer += {0: 0, 1: A, 2: B*2, 3: C*3}[j]
print(answer)