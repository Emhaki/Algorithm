n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
result = []
for i in range(n-7):
    for j in range(m-7):
        black = 0
        white = 0

        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    if graph[a][b] != 'B':
                        black += 1
                    if graph[a][b] != 'W':
                        white += 1
                else:
                    if graph[a][b] != 'W':
                        black += 1
                    if graph[a][b] != 'B':
                        white += 1
        result.append(white)
        result.append(black)

print(min(result))