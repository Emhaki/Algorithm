dic = {}
cnt = 0

for _ in range(int(input())):
    user = input()
    if user == "ENTER":
        for key, value in dic.items():
            if value == 1:
                cnt += 1
        dic = {}
    else:
        if user not in dic:
            dic[user] = 1

for key, value in dic.items():
    if value == 1:
        cnt += 1

print(cnt)