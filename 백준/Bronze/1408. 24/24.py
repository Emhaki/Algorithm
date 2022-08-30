a = list(map(int, input().split(":")))
b = list(map(int, input().split(":")))
t = b[0]*3600 + b[1] * 60 + b[2] - (a[0] * 3600 + a[1] * 60 + a[2])
if t < 0:
    t += 60 * 60 * 24
h = t // 3600
m = (t % 3600) // 60
s = t % 60
print("%02d:%02d:%02d" % (h, m, s))
