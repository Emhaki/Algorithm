from math import ceil

T = int(input())

for _ in range(1, T+1):
    N = int(input())
    card_list = list(map(str, input().split()))
    # card_list = ['A', 'B', 'C', 'D', 'E', 'F']
    # result_lst =['A', 'D', 'B', 'E', 'C', 'F']
    card_first_list = card_list[:ceil(len(card_list)/2)]  # ['A', 'B', 'C']
    card_second_list = card_list[ceil(len(card_list)/2):]  # ['D', 'E', 'F']

    result_list = card_first_list  # ['A', 'B', 'C']
    for i in card_list:  # card_list를 i에 대입
        for j in range(len(card_second_list)):  # 인덱스 위치를 구하기 위한 j
            if i == card_list[j]:  # 만약 card_list의 i와 card_list 인덱스와 같을떄
                # result_list 다음 인덱스에 card_second_list[j]값을 삽입
                result_list.insert(result_list.index(i)+1, card_second_list[j])

    result = " ".join(result_list)
    print(f"#{_} {result}")