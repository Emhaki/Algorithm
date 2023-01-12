def solution(x):
    num = 0
    for i in str(x):
      num += int(i)
    if x % num == 0: answer = True
    else: answer = False
    return answer