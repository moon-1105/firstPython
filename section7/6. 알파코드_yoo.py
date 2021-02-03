
import sys
import math

#sys.stdin=open("in3.txt", "r")

def f_check(v):
    global cnt
    if v == len(N):
        for i in a:
            print(i, end="")
        print()
        cnt += 1
    else:
        if v < len(N):
            tmp = ord('a') - 1
            if int(N[v]) != 0:
                if v == len(N)-1:
                    a.append(chr(int(N[v]) + tmp - 32))
                    f_check(v + 1)
                    a.pop()
                if v < len(N)-1:
                    if int(N[v+1]) != 0:
                        a.append(chr(int(N[v]) + tmp - 32))
                        f_check(v + 1)
                        a.pop()
                    if int(N[v])*10 + int(N[v+1]) < 26:
                        a.append(chr(int(N[v])*10 + int(N[v+1]) + tmp - 32))
                        f_check(v+2)
                        a.pop()
N = list(input())
a = []
cnt = 0
f_check(0)
print(cnt)
