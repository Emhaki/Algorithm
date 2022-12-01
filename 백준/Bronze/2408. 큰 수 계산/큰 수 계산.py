equation = ''
n = int(input())
for _ in range(n + n - 1):
    equation += input()
equation = equation.replace('/', '//') # 나누기 처리
print(eval(equation)) # 문자열 매개변수를 숫자로 변환