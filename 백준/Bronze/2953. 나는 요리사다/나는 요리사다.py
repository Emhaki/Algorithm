player1 = []
player2 = []
player3 = []
player4 = []
player5 = []
n = 0
while n != 5:
    a, b, c, d = map(int, input().split())
    if n == 0:
        player1.append(a)
        player1.append(b)
        player1.append(c)
        player1.append(d)
    elif n == 1:
        player2.append(a)
        player2.append(b)
        player2.append(c)
        player2.append(d)
    elif n == 2:
        player3.append(a)
        player3.append(b)
        player3.append(c)
        player3.append(d)
    elif n == 3:
        player4.append(a)
        player4.append(b)
        player4.append(c)
        player4.append(d)
    elif n == 4:
        player5.append(a)
        player5.append(b)
        player5.append(c)
        player5.append(d)
    n += 1

# player1 = [5, 4, 4, 5]
# player2 = [5, 4, 4, 4]
# player3 = [5, 5, 4, 4]
# player4 = [5, 5, 5, 4]
# player5 = [4, 4, 4, 5]


winner_list = []

winner_list.append(sum(player1))
winner_list.append(sum(player2))
winner_list.append(sum(player3))
winner_list.append(sum(player4))
winner_list.append(sum(player5))

print((winner_list.index(max(winner_list))+1), max(winner_list))