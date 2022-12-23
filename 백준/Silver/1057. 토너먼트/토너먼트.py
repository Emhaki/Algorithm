N, K, I = map(int, input().split())
cnt = 0
while K != I:
  K -= K//2
  I -= I//2
  cnt+=1
print(cnt)