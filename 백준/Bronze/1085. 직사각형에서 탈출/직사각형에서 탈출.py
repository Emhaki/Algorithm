x, y, w, h = map(int, input().split())
result = [w-x, x, y, h-y]
print(min(result))