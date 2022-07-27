# 입력값을 word에 저장
word = str(input())

# 크로아티아 알파벳을 리스트로 선언
cro_word = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

# for문을 통해 크로아티아 알파벳을 i에 삽입
for i in cro_word:
    # 입력된 알파벳 중 i(크로아티아 알파벳)을 'a'로 변경해서 word에 저장
    word = word.replace(i, 'a')

# word의 길이를 출력하면 크로아티아 알파벳은 1로 계산 됨
print(len(word))