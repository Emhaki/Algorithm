# 셀프 넘버 함수를 정의
def self_number(num):
    self_num = num
    while num != 0:
        self_num += num % 10  # 오른쪽 끝 숫자를 더함
        num //= 10  # 오른쪽 끝 숫자를 삭제
    return self_num


result = []
for i in list(range(1, 10001)):
    result.append(self_number(i))  # 셀프 넘버를 저장
    if i not in result:  # 셀프 넘버로 넘어온 값이 1~i 숫자중에 없는지 확인
        print(i)