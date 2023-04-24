def solution(name, yearing, photo):
    answer = []
    dic_ = {}
    for _ in range(len(name)):
        dic_[name.pop()] = yearing.pop()
    # 	{'radi': 3, 'kain': 1, 'kein': 10, 'may': 5}
    for i in photo:
        cnt = 0
        for j in i:
            if j in dic_:
                cnt += dic_[j]
        answer.append(cnt)

    return answer