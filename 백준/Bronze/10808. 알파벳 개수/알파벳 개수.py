word = str(input())
list_ = [0]*26
word_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 'n', "o", 'p', 'q', 'r', 's', 't', 'u', 'v', "w", "x", "y", 'z']

for i in word:
  if i in word_list:
    list_[word_list.index(i)] += 1
print(*list_)