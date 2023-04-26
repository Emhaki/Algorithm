str = input()
word = ''
upper_str = str.upper()
lower_str = str.lower()
for i in range(len(str)):
    if str[i] == upper_str[i]:
        word += str[i].lower()
    else:
        word += str[i].upper()
print(word)