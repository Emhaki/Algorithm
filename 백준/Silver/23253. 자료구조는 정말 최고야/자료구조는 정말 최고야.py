from sys import stdin

# 1. 입력
# 1) 초기값 입력
N, M = map(int, stdin.readline().split())

# 2. 선언
# 1) is_order_possible: 정렬 가능 여부
is_order_possible = True

# 3. 연산 
for _ in range(M):
    stdin.readline()
    # 1) 책 더미 입력
    input_list = list(map(int, stdin.readline().split()))
    # 2) 책 더미의 정렬 여부 확인
    if input_list != sorted(input_list, reverse=True):
        # (1) 정렬 불가할 때 
        # 2 - 1 에 기입 후 break
        is_order_possible = False
        break

# 4. 출력
if is_order_possible:
    print('Yes')
else:
    print('No')