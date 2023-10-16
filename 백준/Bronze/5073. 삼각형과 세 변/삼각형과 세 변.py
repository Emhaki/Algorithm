while True:
    a, b, c = map(int, input().split())
    list_ = []
    
    if a == 0 and b == 0 and c == 0:
        break
    # 세변이 같을 때
    if a == b == c:
        print("Equilateral")
    # 세변이 다 다를 때 
    elif a != b and b != c and c != a:
        list_.append(a)
        list_.append(b)
        list_.append(c)
        long = max(list_)
        list_.pop(list_.index(long))
        if long >= sum(list_):
            print("Invalid")
            
        else:
            print("Scalene")

    elif a == b or b == c or c == a:
        list_.append(a)
        list_.append(b)
        list_.append(c)
        long = max(list_)
        list_.pop(list_.index(long))
        if long >= sum(list_):
            print("Invalid")
        else:
            print("Isosceles")