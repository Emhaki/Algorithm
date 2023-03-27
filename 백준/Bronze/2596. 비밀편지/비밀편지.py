if __name__ == '__main__':
    n = int(input())
    s = input()
    s_li = []
    for i in range(0, n * 6, 6):
        s_li.append(s[i: i + 6])
    promise = ['000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010']

    correct = ''
    incorrect = 0
    for i in s_li:
        incorrect = 0
        for j in promise:
            cnt = 0  # 맞은 개수
            for k in range(6):
                if i[k] == j[k]:
                    cnt += 1
            if cnt >= 5:  # 똑같거나 한 자만 다른 경우
                correct += chr(promise.index(j) + 65)
                break
            else:  # 두 자 이상 다른 경우
                incorrect += 1
        if incorrect == len(promise):
            print(s_li.index(i) + 1)
            quit()
    print(correct)