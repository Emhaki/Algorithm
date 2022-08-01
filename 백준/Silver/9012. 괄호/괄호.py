T = int(input())

# (())())
for i in range(T):
    word = input()
    word_list = list(word)
    sum = 0
    for i in word_list:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')