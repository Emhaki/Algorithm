M = int(input())
N = int(input())

sosu_list = []
for num in range(M, N+1): # M이상 ~ N이하의 수
    count = 0 # 나눠지는 수가 있으면 카운트
    if num > 1: # 2이상의 수들 중에 소수를 찾는다.
        for i in range(2, num): # 2~num에서 나눠지는 수를 찾는다
            if num % i == 0: # 나머지가 0이면 나눠지는 수(소수 아님)
                count += 1 # 소수가 아님을 카운트
                break
        if count == 0: # 나눠지는 수가 없으면 소수
            sosu_list.append(num)


if len(sosu_list) > 0:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)