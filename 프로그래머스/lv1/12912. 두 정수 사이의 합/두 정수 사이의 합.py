def solution(a, b):
    answer = 0
    if a < b :
      answer = sum([ answer + i for i in range(a, b+1 )])
    else:
      answer = sum([ answer + i for i in range(b, a+1 )])
    return answer