pay = 1000 - int(input())
changes = [500, 100, 50, 10, 5, 1]
cnt = 0
for change in changes:
  if pay == 0:
    break
  cnt += pay // change # 몫의 값을 cnt에 더함 
  pay %= change # 거스름돈에 동전을 나눈값을 거스름돈으로 저장

print(cnt)