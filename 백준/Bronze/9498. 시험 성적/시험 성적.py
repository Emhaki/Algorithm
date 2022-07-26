a = int(input())

if a >= 90:
    print('A')
elif a >= 80 and 90 > a:
    print('B')
elif a >= 70 and 80 > a:
    print('C')
elif a >= 60 and 70 > a:
    print('D')
else:
    print('F')