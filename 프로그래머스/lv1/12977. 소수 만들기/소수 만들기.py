def solution(nums):
    from itertools import combinations
    answer = 0
    nums.sort()
    
    for i in combinations(nums, 3):
        result = True
        for j in range(2, int(sum(i)**0.5) + 1):
            if sum(i) % j == 0:
                result = False
                break
        if result == True:
            answer += 1      

    return answer