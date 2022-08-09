R, C = map(int, input().split())

parking_lot = []
for _ in range(R):
    parking_lot.append(input())
# parking_lot = ['#..#', '..X.', '..X.', '#XX#']

crush_zero = 0
crush_one = 0
crush_two = 0
crush_three = 0
crush_four = 0

for r in range(R):
    for c in range(C):
        if r+1 == R or c+1 == C:
            break
        w = parking_lot[r][c]
        x = parking_lot[r][c+1]
        y = parking_lot[r+1][c]
        z = parking_lot[r+1][c+1]

        temp = w+x+y+z

        if "#" in temp:
            continue
        else:
            monster_car = temp.count("X")
            if monster_car == 0:
                crush_zero += 1
            elif monster_car == 1:
                crush_one += 1
            elif monster_car == 2:
                crush_two += 1
            elif monster_car == 3:
                crush_three += 1
            elif monster_car == 4:
                crush_four += 1
print(crush_zero)
print(crush_one)
print(crush_two)
print(crush_three)
print(crush_four)