T = int(input())

for _ in range(T):
    price_s = int(input())
    option = int(input())
    for _ in range(option):
        q, p = map(int, input().split())
        add_price = q*p
        price_s += add_price
    print(price_s)