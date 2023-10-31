import sys
input = sys.stdin.readline

N = int(input().rstrip())
vote = []

for i in range(N):
    vote.append(int(input()))

count = 0
while True:
    if N == 1:
        break
    # Max값과 다솜이값이 같을 때
    if max(vote) <= vote[0] and vote.count(vote[0]) == 1:
        break
    elif max(vote) <= vote[0] and vote.count(vote[0]) >= 2:
        count += 1
        break
    
    target = vote.index(max(vote))    
    vote[target] -= 1
    vote[0] += 1
    count += 1

print(count)