import sys
input = sys.stdin.readline

N = int(input().rstrip())
list_ = list(map(str, input().split()))
pizza = {}
pizza_num = 0

for i in list_:
    if i[-6:] == 'Cheese':
        if i not in pizza:
            pizza[i] = 1
            pizza_num += 1

if pizza_num >= 4:
    print("yummy")
else:
    print("sad")