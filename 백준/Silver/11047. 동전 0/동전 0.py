N, K = map(int, input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True) # 내림차순으로 변경경

result=0
for i in coins:
    if K==0: 
      break
    result += K//i # 나눠지지 않으면 0
    K %= i
    
print(result)