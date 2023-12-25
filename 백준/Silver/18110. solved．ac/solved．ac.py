import sys
input = sys.stdin.readline

# 반올림을 계산하는 함수
# 파이썬의 반올림 내장함수(round)는 오사오입이다.
# 따라서, 사사오입을 위한 반올림 함수를 따로 정의해야한다.
def round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

# 난이도 의견의 개수
n = int(input())  

if n:
    # 사용자들이 제출한 난이도 의견 목록을 정렬하여 opinion에 저장
    opinion = sorted([int(input()) for _ in range(n)])
    # 제외되어야 하는 사람의 수 계산
    start = round(n * 0.15)  
    # 제외되지 않은 의견으로 계산된 평균을 구할 범위 선택
    score = opinion[start:n - start]  
    # 평균을 계산하고 반올림하여 출력
    print(round(sum(score) / len(score)))  
else: # 의견이 없을 경우
    print(0)