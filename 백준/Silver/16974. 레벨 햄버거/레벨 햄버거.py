N, X = map(int, input().split())

burger = [1] * 51            # 버거의 레이아웃 갯수
patty = [1] * 51             # 버거의 패티 갯수


for i in range(1, N+1):
    burger[i] = 1 + burger[i-1] + 1 + burger[i-1] + 1
    patty[i] = patty[i-1] + 1 + patty[i-1]


def eat(n, x):                      # 먹은 패티 갯수
    if n == 0:
        return x
    if x == 1:
        return 0
    elif x <= 1 + burger[n-1]:						# case 1
        return eat(n-1, x-1)                # 맨 아래 번 빼고 (x-1)
    elif x == 1 + burger[n-1] + 1:                  # case 2 딱 ~가운데 패티까지 먹은 경우
        return patty[n-1] + 1
    elif x <= burger[n-1] + burger[n-1] + 1 + 1:	# case 3
        return patty[n-1] + 1 + eat(n-1, (x-(burger[n-1]+2)))
    else:											# case 4
        return patty[n]

print(eat(N, X))