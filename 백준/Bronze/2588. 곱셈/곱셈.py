a = list(map(int, input()))
b = list(map(int, input()))

a_num = int(str(a[0])+str(a[1])+str(a[2]))
b_num = int(str(b[0])+str(b[1])+str(b[2]))

result1 = (a_num*b[0]*100)
result2 = (a_num*b[1]*10)
result3 = a_num*b[2]
print(a_num*b[2])
print(a_num*b[1])
print(a_num*b[0])
print(result1+result2+result3)