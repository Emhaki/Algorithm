N, X = map(int, input().split())
blog = list(map(int, input().split()))

if max(blog) == 0:
    print("SAD")
else:
    value = sum(blog[:X])

    max_value = value # 5
    max_cnt = 1

    for i in range(X, N):
        value += blog[i]
        value -= blog[i-X]

        if value > max_value:
            max_value = value
            max_cnt = 1
        
        elif value == max_value:
            max_cnt += 1
    
    print(max_value)
    print(max_cnt)