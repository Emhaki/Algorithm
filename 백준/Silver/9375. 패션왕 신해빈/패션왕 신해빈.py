T = int(input())
for _ in range(T):
    clothes = {}

    n = int(input())
    for _ in range(n):
        v, k = input().split()

        if clothes.get(k) == None:
            clothes[k] = set()
        clothes[k].add(v)

    count = 1
    for key in clothes.keys():
        count *= len(clothes[key]) + 1
    print(count - 1)