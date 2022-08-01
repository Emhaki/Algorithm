N = str(input())

result = N.split("-")
result_word = ""

for i in range(0, len(result)):
    result_word = result[i][0]
    print(result_word, end="")