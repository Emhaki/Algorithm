from itertools import *
def solution(babbling):
    answer = 0
    list_ = ["aya", "ye", "woo", "ma"]
    word = []
    for i in range(1, len(list_)+1): # 1~4개의 조합
      for j in permutations(list_, i): # 1~4개의 조합
        word.append(''.join(j)) # 모든 조합을 합치기 
      
    for i in babbling:
      if i in word:
        answer += 1

    return answer