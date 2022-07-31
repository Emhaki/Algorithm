# 입력값을 숫자형과 list에 담기도록 설정
T = list(map(int, input().split()))

# 만약 입력된 값들이 순차적으로 오른다면 ascending
if T == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
# 거꾸로 내림차순이라면 descending
elif T == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
# 혼종이면 mixed
else:
    print("mixed")