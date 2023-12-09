import sys
input = sys.stdin.readline

# 거리가 D인 문자열
# 문자열의 길이가 N일 때, 0쌍부터 N-2쌍까지 정의
# 모든 문자열쌍에서 유일할 경우 놀라운 문자열

while True:
    word = str(input().strip())
    if word == "*":
        break
    # 입력받은 문자의 길이 체크
    # 인덱스의 범위가 넘어가지 않게끔 컨트롤
    # 거리만큼 인덱스 확인
    # 문자열이 중복된 점이 있는지 체크
    

    if len(word) == 1:
        print(f"{word} is surprising.")
        continue
    
    for i in range(1, len(word)-1):
        result = []
        for j in range(len(word)-i):
            unique = word[j]+word[i+j]
            if unique not in result:
                result.append(unique)
            
            else:
                print(f"{word} is NOT surprising.")
                break
        else:
            continue
        break
    else:
        print(f"{word} is surprising.")