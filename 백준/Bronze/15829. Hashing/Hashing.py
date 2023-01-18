L = int(input())
M = 1234567891
R = 31
hashing = input()

answer = 0

for i in range(len(hashing)):
    num = ord(hashing[i]) - 96
    answer += num * (R**i)

print(answer % M)