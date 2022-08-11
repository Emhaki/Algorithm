S, K, H = map(int, input().split())

list_ = [S, K, H]


if sum(list_) >= 100:
    print("OK")
else:
    if list_.index(min(list_)) == 0:
        print("Soongsil")
    elif list_.index(min(list_)) == 1:
        print("Korea")
    elif list_.index(min(list_)) == 2:
        print("Hanyang")