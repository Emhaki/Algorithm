a = int(input())
b = int(input())
c = int(input())
# a, b, c를 차례로 받아준다.
result = list(str(a * b * c))
# result에 a,b,c,곱을 str로 변환하고 list로 형 변환시켜준다.
for i in range(10):
    print(result.count(str(i)))