K = str(input())

count_dic = {}
count_dic["문제"] = 0  # 처음부터 고무오리면 "문제"라는 키값이 없으므로 생성
while True:
    N = str(input())
    if N == "고무오리 디버깅 끝":
        break
    if N == "문제":
        count_dic[N] += 1
    elif N == "고무오리" and count_dic["문제"] == 0:
        count_dic["문제"] += 2
    elif N == "고무오리" and count_dic["문제"] != 0:
        count_dic["문제"] -= 1
# {'문제': 0}

if count_dic["문제"] == 0:
    print("고무오리야 사랑해")
elif count_dic["문제"] != 0:
    print("힝구")