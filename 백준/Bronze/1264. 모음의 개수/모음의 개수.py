word = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    try:
        word_list = list(map(str, input().split()))
        if word_list[0] == '#':
            break
        else:
            count = 0
            for i in word_list:
                for j in str(i):
                    if j in word:
                        count += 1

            print(count)
    except EOFError:
        break