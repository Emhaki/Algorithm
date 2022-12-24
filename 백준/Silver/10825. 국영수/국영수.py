N = int(input())
students = [] # 학생 정보를 담는 리스트

for _ in range(N):
  students.append(input().split())

# 정렬 기준
# 1. 두 번째 원소를 기준으로 내림차순 정렬
# 2. 두 번째 원소가 같을 경우, 세 번째 원소를 기준으로 오름차순 정렬
# 3. 세 번째 원소가 같을 경우, 네 번째 원소를 기준으로 내림차순 정렬
# 4. 네 번째 원소가 같을 경우, 첫 번째 원소를 기준으로 오름차순 정렬

# -는 내림차순, +는 오름차순
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
  print(student[0])