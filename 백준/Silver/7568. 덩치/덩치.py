N = int(input())
data = []
winner_list = []

for i in range(1, N+1):
    x, y = list(map(int, input().split()))
    data.append((x, y))

for i in range(N):
    count = 0
    for j in range(N):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    winner_list.append(count + 1)

for d in winner_list:
    print(d, end=" ")