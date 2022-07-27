word = input().upper()
# MISSISSIPI

# 중복을 없애기 위해 set 사용
word_set = list(set(word))
# ['I', 'M', 'P', 'S']

count_list = []

for i in word_set:
    # word_set 리스트에 모아뒀던 단어들을 i에 넘겨주면서
    # 입력한 word에 i의 갯수를 count_list에 추가
    count_list.append(word.count(i))
    # count_list = [4, 1, 1, 4]
    # M 1개, S 4개, I 4개, P 1개
    # 같은 단어가 있다면 1보다 높음

if count_list.count(max(count_list)) > 1:
    # count_list.count(4)
    # 만약 count_list에 동일한 max값이 있다면 count_list는 2개 이상
    # 2개
    print("?")
else:
    # count_list의 가장 큰값의 인덱스를 반환
    # 반환한 값을 통해 word_set['word']의 값 출력
    print(word_set[count_list.index(max(count_list))])