
import sys
import math
from collections import deque
# heapq를 사용할 수 있도록 추가
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_DFS(v):
    if v <= 7:
        print(v, end=' ')
        f_DFS(2*v)
        f_DFS(2*v + 1)
def f_DFS1(v1):
    if v1 <= 7:
        f_DFS1(2*v1)
        print(v1, end=' ')
        f_DFS1(2*v1 + 1)
def f_DFS2(v2):
    if v2 <= 7:
        f_DFS2(2*v2)
        f_DFS2(2 * v2 + 1)
        print(v2, end=' ')


f_DFS(1)
print()
f_DFS1(1)
print()
f_DFS2(1)
