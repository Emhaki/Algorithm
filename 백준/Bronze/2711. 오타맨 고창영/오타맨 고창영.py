T = int(input())

for _ in range(T):
    a, b = input().split()
    b = b.upper()
    input_word = []
    for i in b:
        input_word.append(i)
    # input_word = ['M', 'I', 'S', 'S', 'P', 'E', 'L', 'L']
    # 입력된 a값에 -1을 통해 원하는 인덱스를 pop
    input_word.pop(int(a)-1)
    # join 함수를 통해서 리스트에 담긴 값들을 문자열로 변환
    result = ''.join(input_word)
    print(result)