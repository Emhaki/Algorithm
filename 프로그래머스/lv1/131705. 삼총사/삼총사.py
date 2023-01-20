def solution(number):
    from itertools import combinations
    result = list(combinations(number, 3))
    answer = 0
    for i in result:
        if sum(i) == 0:
          answer += 1
    return answer