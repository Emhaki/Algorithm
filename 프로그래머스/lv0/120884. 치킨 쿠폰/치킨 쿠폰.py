def solution(chicken):
    answer = 0
    coupon = 0
    
    answer += chicken // 10
    coupon += chicken // 10 # 108
    coupon += chicken % 10
    while coupon >= 10:
        coupon -= 10
        answer += 1
        coupon += 1

    return answer