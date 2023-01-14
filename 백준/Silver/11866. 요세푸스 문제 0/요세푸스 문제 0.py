a, b = map(int, input().split())

num = [i for i in range(1, a+1)]
result = []
now = b-1
while num:
    result.append(num.pop(now))
    if num:
        now = ((now-1)+b) % len(num)
print(f'<{", ".join(map(str, result))}>')