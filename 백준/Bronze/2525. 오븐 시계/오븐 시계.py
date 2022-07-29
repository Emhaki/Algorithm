H, M = map(int, input().split())
time = int(input())

M = M + time

while M >= 60:
    H += 1
    M -= 60

while H >= 24:
    H -= 24

print(H, M)