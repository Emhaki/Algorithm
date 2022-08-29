N = int(input())
score = list(map(int, input().split()))

garbage_score = max(score)
result_list = []
for i in score:
    result_score = (i / garbage_score) * 100
    result_list.append(result_score)

print(sum(result_list)/len(result_list))