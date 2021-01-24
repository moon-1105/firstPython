
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_check(v, m):
    global cnt
    if v == M:
        for i in l:
            print(i, end=' ')
        print()
        cnt += 1
    else:
        if v < M:
            for i in range(1+v, N+1):
                if b[i] == 0:
                    if a[i-1] > m:
                        m = a[i-1]
                        b[i] = 1
                        l.append(a[i-1])
                        f_check(v + 1, m)
                        b[i] = 0
                        l.remove(a[i-1])

N, M = map(int,input().split())

a = [x for x in range(1, N + 1)]
b = [0] * (N + 1)
l = []
cnt = 0
f_check(0, 0)
print(cnt)
