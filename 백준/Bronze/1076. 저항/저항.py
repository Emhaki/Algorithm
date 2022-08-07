color_value_dic = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9',
}
color_mul_dic = {
    'black': '1',
    'brown': '10',
    'red': '100',
    'orange': '1000',
    'yellow': '10000',
    'green': '100000',
    'blue': '1000000',
    'violet': '10000000',
    'grey': '100000000',
    'white': '1000000000',
}
first_ = str(input())
second_ = str(input())
third_ = str(input())

print(int((str(color_value_dic[first_]) +
      str(color_value_dic[second_])))*int(color_mul_dic[third_]))