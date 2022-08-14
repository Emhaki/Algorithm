for _ in range(3):
    N = int(input())
    list_ = []
    for _ in range(N):
        list_.append(int(input()))

    if sum(list_) > 0:
        print("+")
    elif sum(list_) < 0:
        print("-")
    elif sum(list_) == 0:
        print(0)