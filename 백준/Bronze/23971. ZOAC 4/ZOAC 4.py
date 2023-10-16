import math
H, W, N, M = map(int, input().split())
a = math.ceil(W/(M+1))
b = math.ceil(H/(N+1))
print(a*b)