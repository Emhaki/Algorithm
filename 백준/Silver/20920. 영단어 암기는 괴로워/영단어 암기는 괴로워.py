import sys
input = sys.stdin.readline
N, M = map(int, input().split())
word_list = {}

for _ in range(N):
    word = input().strip()

    if len(word) < M:
        continue
    else: 
        if word not in word_list: # 단어가 있는 경우
            word_list[word] = 1
        else:
            word_list[word] += 1

word_list = sorted(word_list.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in word_list:
    print(i[0])



