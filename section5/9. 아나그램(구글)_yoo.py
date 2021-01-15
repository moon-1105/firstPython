
import sys
import math
from collections import deque

#sys.stdin = open("in4.txt", "rt")
p = dict()
A = list(input())
for k in range(65, 123):
    p[chr(k)] = 0
for i in A:
    p[i] += 1
B = list(input())
for j in B:
    if p[j] > 0:
        p[j] -= 1
    else:
        print("NO")
        sys.exit()
print("YES")
