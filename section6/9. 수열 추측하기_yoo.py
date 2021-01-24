
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_check(v, sum):
    if v == N and F == sum:
        for j in l:
            print(j, end=' ')
        sys.exit(0)
    else:
        if v < N:
            for j in range(1, N + 1):
                if ch[j] == 0:
                    ch[j] = 1
                    l.append(a[j-1])
                    f_check(v + 1, sum + a[j-1] * b[v])
                    ch[j] = 0
                    l.remove(a[j-1])

N, F = map(int, input().split())
a = [k for k in range(1, N+1)]
b = [1] * N
ch = [0] * (N + 1)
l = []
for i in range(1, N):
    b[i] = b[i-1] * (N - i) // i
f_check(0, 0)
