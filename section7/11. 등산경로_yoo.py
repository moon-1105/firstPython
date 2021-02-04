
import sys
import math

#sys.stdin=open("in2.txt", "r")

def f_check(m_x, m_y):
    global cnt
    if m_x == max_x and m_y == max_y:
        cnt += 1
    if m_x < N - 1:
        if a[m_x][m_y] < a[m_x + 1][m_y]:
            f_check(m_x + 1, m_y)
    if m_y < N - 1:
        if a[m_x][m_y] < a[m_x][m_y + 1]:
            f_check(m_x, m_y + 1)
    if m_x > 0:
        if a[m_x][m_y] < a[m_x - 1][m_y]:
            f_check(m_x - 1, m_y)
    if m_y > 0:
        if a[m_x][m_y] < a[m_x][m_y - 1]:
            f_check(m_x, m_y - 1)

N = int(input())
a = [[int(x) for x in map(int, input().split())] for y in range(N)]
cnt = 0
max = a[0][0]
max_x = 0
max_y = 0
min = a[0][0]
min_x = 0
min_y = 0
for i in range(0, N):
    for j in range(0, N):
        if max < a[i][j]:
            max = a[i][j]
            max_x = i
            max_y = j
        if min > a[i][j]:
            min = a[i][j]
            min_x = i
            min_y = j
f_check(min_x,min_y)
print(cnt)
