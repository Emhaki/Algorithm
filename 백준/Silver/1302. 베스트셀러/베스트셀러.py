N = int(input())
dic_ = {}
for _ in range(N):
    name = str(input())
    if name not in dic_:
        dic_[name] = 1  # 만약 dic_에 책 name이 없는 경우 key:name / value 1을 부여
    else:  # 만약 dic_에 name이 있다면 value 값을 1씩 증가
        dic_[name] += 1

best_seller = max(dic_.values())  # 딕셔너리 values값의 max를 저장

result = []

for name, number in dic_.items():  # items를 이용해 key와 value를 name과 number에 할당
    if number == best_seller:  # value인 number와 이전에 저장한 max값과 같다면
        result.append(name)  # 그때의 책을 result 리스트에 append

print(sorted(result)[0])