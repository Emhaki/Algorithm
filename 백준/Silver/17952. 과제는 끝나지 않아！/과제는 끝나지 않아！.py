import sys
input = sys.stdin.readline

task, result = [], 0
for _ in range(int(input())):
    new_task = list(map(int, input().split()))

    if new_task[0] == 1:
        task.append((new_task[1], new_task[2]))

    if task:
        score, time = task.pop()
        time -= 1

        if time == 0:
            result += score
        else:
            task.append((score, time))

print(result)