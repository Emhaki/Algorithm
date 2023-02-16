import sys
input = sys.stdin.readline

N = int(input())
team = list(map(int, input().split()))

team1 = sorted(team)
team2 = sorted(team, reverse=True)

result = []
for i in range(len(team)):
    result.append(team1[i] + team2[i])

print(min(result))