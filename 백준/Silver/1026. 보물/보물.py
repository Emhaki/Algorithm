N = input()
S = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(len(a)):
  S += (min(a) * max(b))

  del a[(a.index(min(a)))]
  del b[(b.index(max(b)))]
print(S)