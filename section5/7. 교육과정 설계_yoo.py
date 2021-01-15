
import sys
import math
from collections import deque

#sys.stdin = open("in2.txt", "rt")

s = list(str(input()))
N = int(input())
check = False
for i in range(0, N):
    check = False
    tmp = deque(s)
    t = tmp.popleft()
    ts = list(str(input()))
    for j in ts:
        if any(j == x for x in tmp):
            break
        if j == t:
            if len(tmp) == 0:
                check = True
                break
            else:
                t = tmp.popleft()
    if check:
        print("#" + str(i + 1) + " YES")
    else:
        print("#" + str(i + 1) + " NO")
