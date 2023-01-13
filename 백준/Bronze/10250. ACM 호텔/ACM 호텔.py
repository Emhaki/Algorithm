import sys
t=int(input())
for _ in range(0,t):
    h,w,n = map(int,sys.stdin.readline().split())
    yy = n % h
    xx = n//h + 1
    if yy==0:
        yy = h
        xx -= 1
    print(yy*100+xx)