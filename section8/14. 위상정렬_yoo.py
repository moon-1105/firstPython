import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

def f_check(n):
    if d[n] == 0:
        for j in range(N):
            if l[n][j] == 1:
                f_check(j)
        d[n] = 1
        c.append(n+1)

N, M = map(int, input().split())
l = [[0] * N for _ in range(N)]
c = []
d = [0] * N
q = deque()
for _ in range(M):
    a, b = map(int, input().split())
    l[b-1][a-1] = 1
for i in range(N):
    f_check(i)
print(c)


