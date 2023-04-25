def solution(s):
    answer = []

    dic_ = {}
    for i in range(len(s)):
        if s[i] not in dic_:
            dic_[s[i]] = i
            answer.append(-1)
        else:
            current = i - dic_[s[i]]
            dic_[s[i]] = i
            answer.append(current)

    return answer