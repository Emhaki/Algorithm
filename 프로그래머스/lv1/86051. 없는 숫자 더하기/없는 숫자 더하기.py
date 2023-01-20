def solution(numbers):
    answer = 0
    list_ = []  
    for i in range(10):
        list_.append(i)
    set_ = {}
    for i in numbers:
        if i not in set_:
            set_[i] = 0
    
    for i in list_:
        if i not in set_:
            answer += i  
    return answer