word = input().upper()
word = list(word)
ben_word = []
result_word = []
for i in "CAMBRIDGE":
    ben_word.append(i)

for j in word:
    if j not in ben_word:
        result_word.append(j)

for i in result_word:
    print(i, end="")