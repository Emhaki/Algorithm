a, b, c = map(int, input().split())
list_ = [a, b, c]
A = min(list_)
C = max(list_)
B = sum(list_) - A - C
k = input()
for i in k:
    if i == 'A':
        print(A, end=' ')
    elif i == 'B':
        print(B, end=' ')
    elif i == 'C':
        print(C, end=' ')