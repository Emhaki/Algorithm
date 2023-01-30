N = int(input())
result = []
for i in range(N):
    result.append(int(input()))

if result.count(1) > result.count(0): print('Junhee is cute!')
else: print('Junhee is not cute!')