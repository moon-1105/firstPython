import sys
import math

#sys.stdin=open("in2.txt", "r")

def f_check(v, s):
    global cnt
    if v == k:
        if s == T:
            cnt += 1
    else:
        if v < k and s <= T:
            for j in range(0, pt[v] + 1):
                f_check(v + 1, s + (pv[v] * j))
T = int(input())
k = int(input())
pv = []
pt = []
cnt = 0
for i in range(0, k):
    a, b = map(int, input().split())
    pv.append(a)
    pt.append(b)
f_check(0, 0)
print(cnt)
