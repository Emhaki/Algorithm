ul_lim = list(map(int, input().split()))
start_link = list(map(int, input().split()))

if_win = False
ul_count = 0
start_count = 0

for i in range(len(ul_lim)):
    ul_count +=  ul_lim[i]
    if ul_count > start_count:
        if_win = True
    start_count += start_link[i]

if if_win == True:
    print("Yes")
else:
    print("No")