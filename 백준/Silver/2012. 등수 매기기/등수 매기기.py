import sys
input = sys.stdin.readline
N = int(input())
grade = []
for i in range(N):
    grade.append(int(input()))

grade.sort()
result = 0
for i in range(1, len(grade)+1):
    result += abs(i - grade[i-1])

print(result)