
import sys
import math
from collections import deque

#sys.stdin = open("in2.txt", "rt")

N = int(input())
l = []
r = []
for i in range(0, N):
    l.append(str(input()))
for j in range(0, N-1):
    r.append(str(input()))
for x in l:
    if not any(x == y for y in r):
        print(x)
