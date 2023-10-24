import sys
input = sys.stdin.readline

N = int(input().rstrip())

check = {}
cnt = 0
for i in range(N):
    a, b = map(str, input().strip().split(" "))
    if a not in check and b == "1":
        check[a] = 1
    elif a not in check and b == "0":
        cnt += 1
    elif a in check and b == "1":
        cnt += 1
    elif a in check and b == "0":
        check.pop(f"{a}", None)

print(cnt + len(check))