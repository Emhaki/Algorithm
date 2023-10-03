N, L = map(int, input().split())
height = list(map(int, input().split()))
height.sort()

for i in range(N):
    if L >= height[i]:
        L += 1
print(L)