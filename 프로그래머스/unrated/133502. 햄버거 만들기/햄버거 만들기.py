def solution(ingredient):
    answer = 0
    stack = []

    for burger in ingredient:
      stack.append(burger)

      if len(stack) >= 4:
        bread2 = stack[len(stack)-4] # 1
        veg = stack[len(stack)-3] # 2
        meat = stack[len(stack)-2] # 3
        bread1 = stack[len(stack)-1] # 1

        if bread1 == 1 and meat == 3 and veg == 2 and bread2 == 1:
          for _ in range(4):
            stack.pop()
          answer += 1
    return answer