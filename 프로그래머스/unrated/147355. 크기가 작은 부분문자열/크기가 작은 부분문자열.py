def solution(t, p):
    answer = 0
    length = len(p)
    len_t = len(t)

    # 문자열탐색범위 5
    len_t -= length
    number_list = []

    for i in range(len_t+1):
        number_list.append(int(t[i:length+i]))

    for x in number_list:
        if x <= int(p):
            answer += 1

    return answer