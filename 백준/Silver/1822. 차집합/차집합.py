A, B = map(int, input().split())

list_A = set(map(int, input().split()))
list_B = set(map(int, input().split()))

res = list_A-list_B

if res:
    print(len(res))
    print(*sorted(list(res)))
else:
    print(0)