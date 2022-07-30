A_list = list(map(int, input().split()))

for i in range(1, 7):
    if A_list.count(i) == 3:
        print(int(f"{i}")*1000+10000)
    elif A_list.count(i) == 2:
        print(int(f"{i}")*100 + 1000)
    elif (A_list[0] != A_list[1] and A_list[1] != A_list[2] and A_list[0] != A_list[2]):
        print(max(A_list)*100)
        break