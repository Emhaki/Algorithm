import sys
input = sys.stdin.readline

word = input().rstrip()
word_list = []
tag = False
res = ''

# 핵심은 <>값을 어떻게 처리할 것인가. 
for i in word:
    # 공백이면 word_list 비움
    if i == ' ':
        while word_list:
            res += word_list.pop()
        res += i
    
    # < 안 단어는 뒤집지 않음, tag값 변경
    elif i == '<':
        while word_list:
            res += word_list.pop()
        tag = True
        res += i
    # 태그 값 변경
    elif i == '>':
        tag = False
        res += i

    # tag가 False라면 태그를 만나지 않았으므로 더해준다.
    elif tag:
        res += i

    # 태그 밖 단어는 뒤집는다
    else:
        word_list.append(i)

while word_list:
    res += word_list.pop()

print(res)