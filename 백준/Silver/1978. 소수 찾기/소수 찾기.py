n = int(input()) # 입력받을 숫자의 개수
nums = list(map(int, input().split(' '))) # 공백으로 숫자 구분. ex) 1 3 5 7
resCnt = 0 # 소수의 개수

for i in nums:
    cnt = 0 
    if(i == 1): # 1은 소수가 아니기 때문에 건너띔
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            cnt += 1
    if(cnt == 1):
        resCnt += 1
print(resCnt)
