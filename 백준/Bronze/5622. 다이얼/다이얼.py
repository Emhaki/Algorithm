N = input().upper()
N = list(N)
cnt = 0
for i in N:
    if i == "A" or i == "B" or i == "C":
        cnt += 3
    elif i == "D" or i == "E" or i == "F":
        cnt += 4
    elif i == "G" or i == "H" or i == "I":
        cnt += 5
    elif i == "J" or i == "K" or i == "L":
        cnt += 6
    elif i == "M" or i == "N" or i == "O":
        cnt += 7
    elif i == "P" or i == "Q" or i == "R" or i == "S":
        cnt += 8
    elif i == "T" or i == "U" or i == "V":
        cnt += 9
    elif i == "W" or i == "X" or i == "Y" or i == "Z":
        cnt += 10
    else:
        cnt += 11
print(cnt)