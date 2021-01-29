
import sys
#sys.stdin=open("in1.txt", "r")

def f_check(v, s, t):
    global m
    if v == N and s <= M:
        if m < t:
            m = t
    else:
        if v < N:
            f_check(v+1, s + pt[v], t + pv[v])
            f_check(v+1, s, t)
N, M = map(int, input().split())
pv = []
pt = []
m = 0
for i in range(0, N):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)
f_check(0, 0, 0)
print(m)
