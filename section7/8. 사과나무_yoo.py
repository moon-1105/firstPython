
import sys
import math

#sys.stdin=open("in1.txt", "r")

def f_check(v, t):
    global cnt
    if v < N:
        for i in range(N//2 - t, N//2 + t + 1):
            cnt += a[v][i]
        if v < N // 2:
            t += 1
        else:
            t -= 1
        f_check(v+1, t)

N = int(input())
a = [[int(x) for x in map(int, input().split())] for y in range(N)]
cnt = 0
f_check(0, 0)
print(cnt)
