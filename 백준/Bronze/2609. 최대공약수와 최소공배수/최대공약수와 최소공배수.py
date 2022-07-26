a, b = map(int, input().split())

a_result = []
b_result = []
c_result = []

for a_least in range(1, 10001):
    if a % a_least == 0:
        a_result.append(a_least)


for b_least in range(1, 10001):
    if b % b_least == 0:
        b_result.append(b_least)

# a_result = [1, 2, 3, 4, 6, 8, 12, 24]
# b_result = [1, 2, 3, 6, 9, 18]
for i in (a_result):
    for j in (b_result):
        if i == j:
            c_result.append(i)

print(max(c_result))
print(a*b//max(c_result))