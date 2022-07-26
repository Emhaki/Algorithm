a,b = (input().split())
a = int(a)
b = int(b)

from math import gcd

GCD = gcd(a, b)
LCM = a * b // GCD

print(GCD)
print(LCM)