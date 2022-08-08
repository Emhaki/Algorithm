N = int(input())

num = 666
count = 1
while True:
    if N == 1:
        break

    num += 1
    temp = str(num)

    if '666' in temp:
        count += 1
    if count == N:
        break
print(num)