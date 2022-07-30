def hansu(n):
    if n < 100:
        return n
    else:
        cnt = 99
        for i in range(100, n+1):
            n_list = list(map(int, str(i)))
            if n_list[0] - n_list[1] == n_list[1] - n_list[2]:
                cnt += 1
        return cnt


n = int(input())
print(hansu(n))