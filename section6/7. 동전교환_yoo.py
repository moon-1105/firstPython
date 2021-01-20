
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_exchange(v, m, c):
    global cnt
    if c < cnt:
        if v == N:
            if m == 0 and cnt > c:
                cnt = c
        else:
            for i in range(0, m//l[v] + 1):
                if c + i > cnt:
                    break
                f_exchange(v+1, m - (l[v] * i), c + i)

N = int(input())
l = list(map(int, input().split()))
M = int(input())
li = [0] * N
l.sort(reverse=True)
cnt = M
f_exchange(0, M, 0)
print(cnt)
