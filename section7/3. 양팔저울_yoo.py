
import sys
import math

#sys.stdin=open("in1.txt", "r")

def f_check(v,s):
    if s > 0:
        if a[s - 1] == 0:
            a[s - 1] = 1
    if v < N:
        f_check(v+1, s - l[v])
        f_check(v+1, s)
        f_check(v+1, s + l[v])

N = int(input())
l = list(map(int, input().split()))
s = sum(l)
a = [0] * s
cnt = 0
f_check(0, 0)
for i in range(0, s):
    if a[i] == 0:
        cnt += 1
print(cnt)
