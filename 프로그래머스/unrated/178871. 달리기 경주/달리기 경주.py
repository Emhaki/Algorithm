def solution(players, callings):
    players_map = {each: index for index, each in enumerate(players)}
    for player in callings:
        index = players_map[player]
        players_map[player] -= 1
        players_map[players[index - 1]] += 1
        players[index - 1], players[index] = players[index], players[index - 1]
    return players