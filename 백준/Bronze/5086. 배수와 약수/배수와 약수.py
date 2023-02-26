while True:
    a,b=map(int, input().split())
    if (a,b)==(0,0):
        break
    if a//b>0 and a%b==0:
        print('multiple')
    elif b//a>0 and b%a==0:
        print('factor')
    else:
        print('neither')