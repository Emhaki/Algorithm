set = [0] * 9
num = list(map(int, str(input())))  #방 번호
# 리스트에서 max값을 찾기
for i in num:
    if i == 6 or i == 9:
        set[6] += 1  #6으로 값 몰아주기
    else:
        set[i] += 1 # 6과 9가 아니라면 각 인덱스에 +1

#6 + 9의 개수가 짝수인지 홀수인지 확인
if set[6] % 2 == 0:
    set[6] = set[6] // 2
else:
    set[6] = (set[6] // 2) + 1

print(max(set))