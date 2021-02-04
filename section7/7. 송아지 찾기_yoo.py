
import sys
import math

#sys.stdin=open("in3.txt", "r")

def f_check(v, t):
    global cnt
    if v == E:
        if cnt > t:
            cnt = t
    elif v > E:
        f_check(v-1, t+1)
    else:
        t += (E - v) // 5
        v += (E - v) - (E - v) % 5
        if v == E:
            if cnt > t:
                cnt = t
        f_check(v+1, t+1)
        f_check(v+5, t+1)
S, E = map(int, input().split())
cnt = 10000
f_check(S, 0)
print(cnt)
