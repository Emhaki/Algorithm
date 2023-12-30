import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poketmon_dict = {}
list_ = []
for i in range(N):
    list_.append(str(input().strip()))
for idx, monster in enumerate(list_):
    poketmon_dict[str(idx+1)] = monster
    poketmon_dict[monster] = str(idx+1)

for k in range(M):
    check = input().strip()
    if check.isdigit():
        print(poketmon_dict[str(check)])
    else:
        print(poketmon_dict[check])