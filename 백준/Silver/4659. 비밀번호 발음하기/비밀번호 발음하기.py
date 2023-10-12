mo_word = ["a", "e", "i", "o", "u"]
while True:
    word = str(input().strip())
    if word == "end":
        break
    count, x, y = 0, 0, 0
    # 1. 모음 하나 포함
    for i in word:
        # 포함여부 확인
        if i in mo_word:
            count += 1
    if count < 1:
        print(f'<{word}> is not acceptable.')
        continue
    # 2. 모음이 3개 혹은 자음이 3개 연속 x
    for i in range(len(word) - 2):
        if word[i] in mo_word and word[i+1] in mo_word and word[i+2] in mo_word:
            x = 1
        elif not(word[i] in mo_word) and not(word[i+1] in mo_word) and not(word[i+2] in mo_word):
            x = 1
    if x == 1:
        print(f'<{word}> is not acceptable.')
        continue
    # 3. 같은 글자가 연속으로 두번 x but ee나 oo 는 허용
    for j in range(len(word)-1):
        if word[j+1] == word[j]:
            if word[j] == "e" or word[j] == "o":
                continue
            else:
                y = 1
    if y == 1:
        print(f'<{word}> is not acceptable.')
        continue
            
    print(f'<{word}> is acceptable.')