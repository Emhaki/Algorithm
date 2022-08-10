list_ = list(map(str, input().split(':')))

happy = 0
sad = 0
for i in list_:
    if i[:2] == '-)':
        happy += 1
    elif i[:2] == '-(':
        sad += 1


if happy == 0 and sad == 0:
    print('none')
elif happy - sad == 0:
    print('unsure')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')