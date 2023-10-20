C, R = map(int, input().split())
K = int(input().strip())

seat = [[0] * C for _ in range(R)]

# [
# [0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0], 
# [0, 0, 0, 0, 0, 0, 0]
# ]

if K > R*C:
    print(0)
    exit()

direction, x, y = 0, 0, 0
dx = [0,1,0,-1]
dy = [-1,0,1,0]

for i in range(1, C*R + 1):
    if i == K:
        print(y+1, x+1)
        break
    else:
        seat[x][y] = i
    
        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= R or y >= C or seat[x][y]:
            x -= dx[direction]
            y -= dy[direction]
            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]