T = int(input())

for i in range(T):
    stack = []
    input_word = input()
    for j in input_word:
        if '(' == j:
            # stack 리스트에 쌓아준다.
            stack.append(j)
        elif ')' == j:
            if stack:
                stack.pop()
            else:  # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else:  # break로 끊기지 않고 수행됐을 경우
        if not stack:  # 끊기지 않고 스택이 비어있다면 괄호가 맞은
            print("YES")
        else:  # 스택에 괄호가 들어있다면 NO
            print("NO")