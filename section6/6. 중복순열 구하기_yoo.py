
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")
def f_duplication(m):
    global cnt
    for i in range(1, N + 1):
        l[M - m] = i
        if m == 1:
            for j in l:
                print(j, end=' ')
            cnt += 1
            print()
        if m > 1:
            f_duplication(m-1)

N, M = map(int, input().split())
l = [0] * M
cnt = 0
f_duplication(M)
print(cnt)
