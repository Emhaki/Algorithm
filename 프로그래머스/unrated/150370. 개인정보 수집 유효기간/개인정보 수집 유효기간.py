def solution(today, terms, privacies):
    answer = []
    terms_dic = {}
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])

    for k in terms:
        current_case, current_month = k.split()
        if current_case not in terms_dic:
            terms_dic[current_case] = current_month
    
    for i in range(len(privacies)):
        date, case = privacies[i].split()
        past_year, past_month, past_day = int(privacies[i][0:4]), int(privacies[i][5:7]), int(privacies[i][8:10])
        
        past_month += int(terms_dic[case])

        while past_month > 12:
            past_month -= 12
            past_year += 1
        
        if past_year > year:
            continue

        elif past_year == year:
            if past_month > month:
                continue
            elif past_month == month:
                if past_day > day:
                    continue
        
        answer.append(i+1)

    return answer