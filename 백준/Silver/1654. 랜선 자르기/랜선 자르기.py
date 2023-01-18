import sys
input = sys.stdin.readline

# K 가지고 있는 랜선의 갯수
# N 필요한 랜선 갯수
K, N = map(int, input().split())
already = [int(input()) for _ in range(K)]
start, end = 1, max(already)

while start <= end:
    mid = (start + end) // 2 # 중간 위치
    line = 0
    for i in already:
        line += i // mid # 분할 된 랜선 수

    if line >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)