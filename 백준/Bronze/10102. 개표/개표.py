people = int(input().strip())
vote = input().strip()
A = 0
B = 0
for i in vote:
    if i == "A":
        A += 1
    elif i == "B":
        B += 1

if A > B:
    print("A")
elif A < B:
    print("B")
elif A == B:
    print("Tie")