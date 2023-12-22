import sys
input=sys.stdin.readline
N=int(input())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for i in range(N):
    n=int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if check(n):
            print(n)
            break
        else:
            n+=1