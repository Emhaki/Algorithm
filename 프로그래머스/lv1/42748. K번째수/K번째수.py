def solution(array, commands):
    result = []
    for i in range(len(commands)):
      list_ = array[commands[i][0]-1 : (commands[i][1])]
      new_list = sorted(list_)
      result.append(new_list[commands[i][2]-1])
    return result