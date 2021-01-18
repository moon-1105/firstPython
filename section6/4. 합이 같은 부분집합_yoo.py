
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_check(v):
    if v == N:
        tmp1 = 0
        tmp2 = 0
        for i in range(0, N):
            if a[i] == 1:
                tmp1 += l[i]
            else:
                tmp2 += l[i]
        if tmp1 == tmp2:
            print("YES")
            sys.exit()
    else:
        a[v] = 1
        f_check(v+1)
        a[v] = 0
        f_check(v+1)

N = int(input())
l = list(map(int, input().split()))
a = [0] * (N+1)
f_check(0)
print("NO")
