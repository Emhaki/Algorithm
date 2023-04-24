def calc_1():
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        temp[i] = arr[n-1-i]
    return temp
 
def calc_2():
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[i][m-1-j]
    return temp
 
def calc_3(arr, n, m):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = arr[n-1-j][i]
    return temp
 
def calc_4(arr, n, m):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = arr[j][m - 1 - i]
    return temp
 
def calc_5():
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):    # move position: 1 -> 2
        for j in range(m // 2):
            temp[i][j + m // 2] = arr[i][j]
 
    for i in range(n // 2):    # move position: 2 -> 3
        for j in range(m // 2, m):
            temp[i + n // 2][j] = arr[i][j]
 
    for i in range(n // 2, n):    # move position: 3 -> 4
        for j in range(m // 2, m):
            temp[i][j - m // 2] = arr[i][j]
 
    for i in range(n // 2, n):    # move position: 4 -> 1
        for j in range(m // 2):
            temp[i - n // 2][j] = arr[i][j]
 
    return temp
 
def calc_6():
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):    # move position: 1 -> 4
        for j in range(m // 2):
            temp[i + n // 2][j] = arr[i][j]
 
    for i in range(n // 2, n):    # move position: 4 -> 3
        for j in range(m // 2):
            temp[i][j + m // 2] = arr[i][j]
 
    for i in range(n // 2, n):    # move position: 3 -> 2
        for j in range(m // 2, m):
            temp[i - n // 2][j] = arr[i][j]
 
    for i in range(n // 2):    # move position: 2 -> 1
        for j in range(m // 2, m):
            temp[i][j - m // 2] = arr[i][j]
 
    return temp
 
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
operation = list(map(int, input().split()))
 
for oper in operation:
    if oper == 1:
        arr = calc_1()
    elif oper == 2:
        arr = calc_2()
    elif oper == 3:
        arr = calc_3(arr, n, m)
        n, m = m, n
    elif oper == 4:
        arr = calc_4(arr, n, m)
        n, m = m, n
    elif oper == 5:
        arr = calc_5()
    else:
        arr = calc_6()
 
for i in arr:
    print(*i)