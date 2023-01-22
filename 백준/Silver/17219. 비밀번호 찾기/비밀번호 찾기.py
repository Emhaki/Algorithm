N, M = map(int, input().split())

site_list = {}

for _ in range(N):
    site, ps = input().strip().split()
    site_list[site] = ps

for _ in range(M):
    print(site_list[input().strip()])