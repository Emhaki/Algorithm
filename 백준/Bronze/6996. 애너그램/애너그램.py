N = int(input())

for _ in range(N):
    a, b = map(str, input().split())

    word1 = sorted(list(a))
    word2 = sorted(list(b))

    if word1 == word2:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")