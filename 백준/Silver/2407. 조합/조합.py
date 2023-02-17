import sys
input = sys.stdin.readline
from math import comb

n, m = map(int, input().split())
print(comb(n,m))