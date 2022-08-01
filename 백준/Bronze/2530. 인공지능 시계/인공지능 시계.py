a, b, c = map(int, input().split())
D = int(input())
# 초 분 시 단위로 증가하기 때문에
# while 함수 순서를 아래와 같이 설정
c += D
while c >= 60:
    c -= 60
    b += 1
while b >= 60:
    b -= 60
    a += 1
while a >= 24:
    a -= 24
print(a, b, c)