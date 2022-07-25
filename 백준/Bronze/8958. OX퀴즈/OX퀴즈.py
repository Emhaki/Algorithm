T = int(input())

for i in range(1, T+1):
    c = input()
    s = list(c)
    cnt = 0
    k = 1
    # for문을 통해 만약 j값이랑 O값이랑 같다면
    # cnt 변수에 k를 더해준다. 연속될 경우 k값은 1씩 커진다.
    for j in s:
        if j == "O":
            cnt += k
            k += 1
        else:
            k = 1
    print(cnt)