n = int(input())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
for i in range(1, n):
    for j in range(0, i+1):
        if j == 0:
            graph[i][0] += graph[i-1][0]
        elif j == i:
            graph[i][j] += graph[i-1][j-1]
        else:
            graph[i][j] += max(graph[i-1][j-1], graph[i-1][j])

print(max(graph[n-1]))