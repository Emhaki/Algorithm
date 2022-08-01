K, N, M = map(int, input().split())

result = K*N - M
if result < 0:
    print(0)
else:
    print(result)