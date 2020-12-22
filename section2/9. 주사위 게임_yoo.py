import sys
import math
#sys.stdin=open("in2.txt", "rt")

def value(x):
    if x[0] == x[1] == x[2]:
        return 10000 + x[0] * 1000
    elif x[0] == x[1]:
        return 1000 + x[0] * 100
    elif x[1] == x[2]:
        return 1000 + x[1] * 100
    elif x[2] == x[0]:
        return 1000 + x[2] * 100
    else:
        m = 0
        for i in range(0, 3):
            if m < x[i]:
                m = x[i]
        return m * 100

N = int(input())
m = 0
for i in range(0, N):
    a = list(map(int, input().split()))
    if value(a) > m:
        m = value(a)
print(m)


