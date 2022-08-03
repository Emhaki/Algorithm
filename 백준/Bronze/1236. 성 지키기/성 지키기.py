n, m = map(int, input().split())
array = []

for _ in range(n):
    array.append(input())

row_count, col_count = 0, 0

for i in range(n):
    if 'X' not in array[i]:
        row_count += 1

for j in range(m):
    if "X" not in [array[i][j] for i in range(n)]:
        col_count += 1
print(max(row_count, col_count))