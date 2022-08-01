result_score = 0
N = 5
while N != 0:
    score = int(input())
    if score <= 40:
        score = 40
    result_score += score
    N -= 1

print(result_score//5)