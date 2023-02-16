import sys
input = sys.stdin.readline
T = int(input()) # 테스트 케이스
for _ in range(T):
    day = int(input()) # 날
    price = list(map(int, input().split()))
    benefit = 0

    while True:
        
        if len(price) == 0:
            break
        # [10, 7, 6]
        sell = price.pop()

        for i in reversed(range(len(price))): # 1, 0
            
            if price[i] <= sell:
                benefit += (sell - price[i])
                price.pop()
            else:
                break
    print(benefit)