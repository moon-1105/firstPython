
import sys

#sys.stdin=open("in1.txt", "r")

def f_check(v, t):
    global m
    if v == N:
        if m < t:
            m = t
    else:
        if v < N:
            if v + pv[v] <= N:
                f_check(v+pv[v], t + pt[v])
            f_check(v + 1, t)

N = int(input())
pv = []
pt = []
m = 0
for i in range(0, N):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)
f_check(0, 0)
print(m)
