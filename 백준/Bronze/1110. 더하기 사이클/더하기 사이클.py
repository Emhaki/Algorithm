N = int(input())  #입력받은 값을 int로 바꿈
num = N           #변하는 값
count = 0         #몇 번 사이클인지
 
while True:
    a = num//10
    b = num %10
    c = (a+b)%10
    num = (b*10) + c
    count += 1
    if(num == N):
        break
 
print(count)