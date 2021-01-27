
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_check(v, s, t):
    global cnt
    if s == K:
        if t % M == 0:
            cnt += 1
    else:
        for i in range(v, N):
            f_check(i+1, s+1, t + a[i])

N, K = map(int, input().split())
a = list(map(int, input().split()))
M = int(input())
l = [0] * N
cnt = 0
f_check(0, 0, 0)
print(cnt)
