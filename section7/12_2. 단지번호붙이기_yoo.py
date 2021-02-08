import sys
import math
from collections import deque

#sys.stdin=open("in1.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N = int(input())
a = [list(map(int, input()))for _ in range(N)]
res = []
cnt = 0
Q = deque()
for i in range(N):
    for j in range(N):
        if a[i][j] == 1:
            a[i][j] = 0
            Q.append((i, j))
            cnt = 1
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    xx = tmp[0] + dx[k]
                    yy = tmp[1] + dy[k]
                    if 0 <= xx < N and 0 <= yy < N and a[xx][yy] == 1:
                        a[xx][yy] = 0
                        Q.append((xx, yy))
                        cnt += 1
            res.append(cnt)
print(len(res))
res.sort()
for x in res:
    print(x)
