X, Y = input().split()


def solution(X):
    num_list = []
    for i in str(X):
        num_list.append(i)
        result = num_list[::-1]

    for j in result:
        if j == '-':
            result.insert(0, result[-1])
            result.pop()
            result2 = result
        else:
            result2 = result

    result2 = "".join(result)
    return round(float(result2))


def solution2(Y):
    num_list = []
    for i in str(Y):
        num_list.append(i)
        result = num_list[::-1]

    for j in result:
        if j == '-':
            result.insert(0, result[-1])
            result.pop()
            result2 = result
        else:
            result2 = result

    result2 = "".join(result)
    return round(float(result2))


print(solution(solution(X) + solution2(Y)))