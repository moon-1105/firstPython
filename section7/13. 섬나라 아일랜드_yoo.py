import sys
import math
from collections import deque
#sys.stdin=open("in1.txt", "r")
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, -1, 0, 1, -1, 1, -1, 1]

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
q = deque()
for i in range(N):
    for j in range(N):
        if a[i][j] == 1:
            a[i][j] = 0
            q.append((i, j))
            cnt += 1
            while q:
                tmp = q.popleft()
                for k in range(8):
                    xx = tmp[0] + dx[k]
                    yy = tmp[1] + dy[k]
                    if 0 <= xx < N and 0 <= yy < N and a[xx][yy] == 1:
                        a[xx][yy] = 0
                        q.append((xx, yy))
print(cnt)
