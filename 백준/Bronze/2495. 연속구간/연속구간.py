for _ in range(3):
    n = input()
    cnt = 0

    for i in range(len(n)):
        start = n[i]  # 현재의 위치를 start로 저장

        con = 1
        for k in range(i+1, len(n)):
            if start != n[k]:  # 현재위치값과 다음위치값이 다르면 브레이크
                break

            if start == n[k]:  # 같으면 연속값에 1 추가
                con += 1
        cnt = max(cnt, con)

    print(cnt)