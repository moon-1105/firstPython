

import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_DFS(v, s, m):
    if s > m:
        m = s
    if m == C:
        print(C)
        sys.exit()
    if m < C:
        if v != N-1:
            if C >= s + l[v+1]:
                f_DFS(v + 1, s + l[v + 1], m)
            f_DFS(v+1, s, m)
    a.append(m)

C,N = map(int,input().split())
l = []
a = []
M = 0
for i in range(0, N):
    l.append(int(input()))
    M += l[i]
if M < C:
    print(M)
    sys.exit()
f_DFS(-1, 0, 0)
print(max(a))
