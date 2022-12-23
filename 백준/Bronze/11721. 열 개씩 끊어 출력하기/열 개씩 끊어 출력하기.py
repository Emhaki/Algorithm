word = input()
while len(word) > 0:
  print(word[:10])
  word = word.replace(word[:10],"")