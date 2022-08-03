n, m = map(str, input().split())

result = n.replace('5', '6')
result2 = m.replace('5', '6')
min_result = n.replace('6', '5')
min_result2 = m.replace('6', '5')


print(int(min_result)+int(min_result2), int(result)+int(result2))