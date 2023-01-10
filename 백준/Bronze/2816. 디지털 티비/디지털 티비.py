import sys

cs = []

result = ''

n = int(input())

for i in range(n):
    c = input().strip()
    cs.append(c)


kbs1_index = cs.index('KBS1')

for i in range(kbs1_index):
    result += '1'

for i in range(kbs1_index):
    result += '4'

for i in range(kbs1_index, 0, -1):
    tmp = cs[i-1]
    cs[i-1] = cs[i]
    cs[i] = tmp

kbs2_index = cs.index('KBS2')

for i in range(kbs2_index):
    result += '1'

for i in range(kbs2_index-1):
    result += '4'

print(result)