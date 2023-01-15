T = int(input())

for _ in range(T):
    N, M = map(int, input().split()) # N은 문서의 갯수, M은 궁금한 문서가 몇 번째에 놓여있는지
    queue = list(map(int, input().split()))
    cnt = 0

    while (M != -1):
        if queue[0] == max(queue):
            del queue[0]
            M -= 1
            cnt += 1
        else:
            queue.append(queue[0])
            del queue[0]

            if M == 0:
                M = len(queue) - 1
            else:
                M -= 1
    print(cnt)