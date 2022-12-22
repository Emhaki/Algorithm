N, k = map(int, input().split())
student = list(map(int, input().split()))
student.sort(reverse=True)
print(student[k-1])