N = int(input())
word = list(input())
result_cnt = 0
for i in range(N-1):
  cnt = 0
  compare = word[:]
  similar_word = input()
  for j in similar_word:
    if j in compare:
      compare.remove(j)
    else:
      cnt += 1
  
  if cnt < 2 and len(compare) < 2:
    result_cnt += 1

print(result_cnt)