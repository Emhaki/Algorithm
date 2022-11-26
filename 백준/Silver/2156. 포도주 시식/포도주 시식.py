N = int(input())
array = [0]*10000
for i in range(N):
  array[i]=int(input()) # array에 입력값을 저장

d = [0]*10000
d[0]=array[0] # 첫번째 포도주양
d[1]=array[0]+array[1] # 첫번쨰와 두번째 포도주 합
d[2]=max(array[2]+array[0], array[2]+array[1], d[1])
for i in range(3, N):
  d[i] = max(array[i]+d[i-2], array[i]+array[i-1]+d[i-3], d[i-1])
  # d[3] = max(array[3]+d[1], array[3]+첫번째,두번쨰 포도주합, max(첫번째+세번째/두번째+세번째/첫번째+두번째))
print(max(d))