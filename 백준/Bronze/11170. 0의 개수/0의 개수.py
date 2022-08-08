T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    list_ = []
    for i in range(N, M+1):
        for j in str(i):  # 입력받은 숫자들을 str형태로 변환해서 각각 list_에 append
            list_.append(j)
    # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '0']
    if list_.count('0') > 0:  # str형태이기 때문에 count '0'
        print(list_.count('0'))
    else:
        print(0)