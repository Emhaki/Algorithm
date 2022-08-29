N = int(input())

count = 0
k = 1  # 1부터 노래하기 시작

while N > 0:
    if k > N:  # 만약 불러야 하는 음계가 남아있는 새의 수보다 많다면
        k = 1  # 음계를 1로 초기화
    N -= k  # 부른 음계만큼 새의 수가 감소
    k += 1  # 새가 떠난 뒤 음계를 1씩 올려줌
    count += 1

print(count)