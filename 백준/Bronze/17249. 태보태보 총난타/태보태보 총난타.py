S = list(map(str, input()))
cnt = 0
cnt2 = 0
if "(" in S:
    Q = S.index("(")
    for i in range(0, int(Q)):
        if S[i] == "@":
            cnt += 1
if ")" in S:
    Q1 = S.index(")")
    for j in range(int(Q1), len(S)):
        if S[j] == "@":
            cnt2 += 1

print(cnt, cnt2)