import sys
input = sys.stdin.readline

N, M = map(int, input().split(" "))
word_list = []
result = 0
for _ in range(N):
    word_list.append(input().rstrip())

for _ in range(M):
    word = input().rstrip()
    if word in word_list:
        result += 1
print(result)