import sys
N = int(sys.stdin.readline())
player_dic = {}
for _ in range(N):
    player = str(sys.stdin.readline())
    if player not in player_dic:
        player_dic[player] = 1
    else:
        player_dic[player] += 1
for _ in range(N-1):
    player = str(sys.stdin.readline())
    if player in player_dic:
        player_dic[player] -= 1
# {'mislav': 1, 'stanko': 0, 'ana': 0}
stuffed_player = max(player_dic.values())
for key, value in player_dic.items():
    if value == stuffed_player:
        print(key)