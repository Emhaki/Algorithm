def solution(record):
    answer = []
    kakao_set = dict()
    data_list = [list(i.split()) for i in record]

    for data in data_list:
        if data[0] == 'Enter' or data[0] == 'Change':
            kakao_set[data[1]] = data[2]

    for data in data_list:
        if data[0] == 'Enter':
            answer.append(f"{kakao_set[data[1]]}님이 들어왔습니다.")
        elif data[0] == 'Leave':
            answer.append(f"{kakao_set[data[1]]}님이 나갔습니다.")
    return answer