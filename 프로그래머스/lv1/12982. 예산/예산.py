def solution(d, budget):
    d.sort()
    answer = 0
    cnt = 0
    for i in d:
      answer += i
      if answer <= budget:
        cnt +=1

    return cnt