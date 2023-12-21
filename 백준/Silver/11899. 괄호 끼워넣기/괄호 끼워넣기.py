import sys
input = sys.stdin.readline

word = str(input().strip())
cnt = 0
list_ = []

for i in word:
    if i == "(":
        list_.append(i)
    else:
        if list_:
            list_.pop()
        else:
            cnt += 1
cnt += len(list_)
print(cnt)