
import sys
import math

#sys.stdin=open("in1.txt", "r")

def f_check(v):
    global cnt
    if v == N:
        if b[0] != b[1] and b[1] != b[2] and b[2] != b[0]:
            if cnt > (max(b) - min(b)):
                cnt = (max(b) - min(b))
    else:
        if v < N:
            for j in range(0, 3):
                b[j] += a[v]
                f_check(v + 1)
                b[j] -= a[v]

N = int(input())
a = []
b = [0] * 3
for i in range(0, N):
    a.append(int(input()))
cnt = sum(a)
f_check(0)
print(cnt)
