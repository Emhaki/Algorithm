import sys
input = sys.stdin.readline

N = int(input().strip())

tunnel = {}
cnt = 0

for i in range(N):
    tunnel[input().strip()] = i

for k in range(N):
    out_tunnel = input().strip()
    if next(iter(tunnel)) != out_tunnel:
        cnt += 1
    tunnel.pop(out_tunnel)
print(cnt)