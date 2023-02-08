import sys
input = sys.stdin.readline

N = int(input())

house_list = []
for _ in range(N):
    R, G, B = map(int, input().split())
    house_list.append([R, G, B])
    
for i in range(1, len(house_list)):
    house_list[i][0] = house_list[i][0] + min(house_list[i-1][1], house_list[i-1][2])
    house_list[i][1] = house_list[i][1] + min(house_list[i-1][0], house_list[i-1][2])
    house_list[i][2] = house_list[i][2] + min(house_list[i-1][0], house_list[i-1][1])

print(min(house_list[-1][0], house_list[-1][1], house_list[-1][2]))