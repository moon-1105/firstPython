
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_row(v):
    global cnt
    for i in range(0, N):
        if l[i] == 0:
            l[i] = 1
            a.append(i+1)
            if v == M - 1:
                for j in a:
                    print(j, end=' ')
                print()
                cnt += 1
            else:
                f_row(v+1)
            l[i] = 0
            l[i] = 0
            a.remove(i+1)
N, M = map(int, input().split())
l = [0] * N
a = []
cnt = 0
f_row(0)
print(cnt)
