N, K = map(int, input().split())
student = []
for i in range(N):
  a, b = map(int, input().split())
  student.append([a, b])

m_gender = []
g_gender = []

for j in student:
  if j[0] == 1:
    m_gender.append(j)
  else:
    g_gender.append(j)
m_grade = [0]*6
g_grade = [0]*6

for i in m_gender:
  if i[1] == 1:
    m_grade[0] += 1
  elif i[1] == 2:
    m_grade[1] += 1
  elif i[1] == 3:
    m_grade[2] += 1
  elif i[1] == 4:
    m_grade[3] += 1
  elif i[1] == 5:
    m_grade[4] += 1
  elif i[1] == 6:
    m_grade[5] += 1

for i in g_gender:
  if i[1] == 1:
    g_grade[0] += 1
  elif i[1] == 2:
    g_grade[1] += 1
  elif i[1] == 3:
    g_grade[2] += 1
  elif i[1] == 4:
    g_grade[3] += 1
  elif i[1] == 5:
    g_grade[4] += 1
  elif i[1] == 6:
    g_grade[5] += 1

room = 0
for i in m_grade:
  if i % K == 0:
    room += (i // K)
  else:
    room += i // K + 1

for i in g_grade:
  if i % K == 0:
    room += (i // K)
  else:
    room += i // K + 1

print(room)