N, M = map(int, input().split()) # N 나무의 수, M 가져가야 할 길이
tree = list(map(int, input().split()))
start = 1
end = max(tree)
# [20, 15, 10, 17]
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in tree:
        if i >= mid:
            result += i - mid 

    if result >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)