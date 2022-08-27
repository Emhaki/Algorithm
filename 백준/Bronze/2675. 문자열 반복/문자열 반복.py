n = int(input())
for i in range(n):
    x, y = input().split()
    text = ''
    for i in y:
        text += int(x) * i
    print(text)