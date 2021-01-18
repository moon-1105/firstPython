
import sys
import math
from collections import deque
import heapq as hq

#sys.stdin = open("in1.txt", "rt")

def f_DFS(v):
    if v == N + 1:
        for i in range(1, N + 1):
            if l[i] == 1:
                print(i, end=" ")
        print()
    else:
        l[v] = 1
        f_DFS(v + 1)
        l[v] = 0
        f_DFS(v + 1)

N = int(input())
l = [0] * (N + 1)
f_DFS(1)
