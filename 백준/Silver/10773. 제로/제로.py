K = int(input())
input_list = []
stack = []

for _ in range(K):
    input_list.append(int(input()))

for elem in input_list:
    if elem != 0:
        stack.append(elem)
    else:
        stack.pop()

print(sum(stack))