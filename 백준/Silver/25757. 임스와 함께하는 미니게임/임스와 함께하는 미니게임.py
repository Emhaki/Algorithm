N, kindOf = input().split()
player = [input() for _ in range(int(N))]
player = list(set(player))

if kindOf == 'Y':
    print(len(player))
elif kindOf == 'F':
    print(len(player) // 2)
elif kindOf == 'O':
    print(len(player) // 3)