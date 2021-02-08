
import sys
import math

#sys.stdin=open("in1.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def f_check(m_x, m_y):
    global cnt
    cnt += 1
    a[m_x][m_y] = 0
    for l in range(4):
        xx = m_x + dx[l]
        yy = m_y + dy[l]
        if 0 <= xx < N and 0 <= yy < N and a[xx][yy] == 1:
            f_check(xx, yy)

N = int(input())
a = [list(map(int, input()))for _ in range(N)]
res = []
for i in range(N):
    for j in range(N):
        if a[i][j] == 1:
            cnt = 0
            f_check(i, j)
            res.append(cnt)
print(len(res))
res.sort()
for x in res:
    print(x)
