num = str(input())

cnt = 0
for i in range(len(num)-1): # 11001100110011000001
  if num[i] != num[i+1]: # 현재와 다음이 다를때마다 카운트
    cnt += 1
print((cnt+1)//2)