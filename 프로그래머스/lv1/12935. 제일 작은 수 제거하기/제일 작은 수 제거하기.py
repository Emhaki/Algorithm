def solution(arr):
    answer = []
    for i in arr:
      answer.append(i)

    if len(answer) >= 2:
      k = min(answer)
      answer.pop(answer.index(k))
    else:
      answer = [-1]

    return answer