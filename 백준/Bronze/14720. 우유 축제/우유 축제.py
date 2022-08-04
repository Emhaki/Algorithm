N = int(input())

arr = list(map(int, input().split()))

# arr = [0,1,2,0,1,2]
cnt = 0
for i in range(N):
    if arr[i] == cnt % 3:
        cnt += 1


print(cnt)