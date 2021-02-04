
import sys
import math

#sys.stdin=open("in1.txt", "r")
def f_check(m_x, m_y):
    global cnt
    if m_x == 6 and m_y == 6:
        cnt += 1
    if m_x < 6:
        if a[m_x+1][m_y] == 0:
            a[m_x+1][m_y] = 1
            f_check(m_x + 1, m_y)
            a[m_x + 1][m_y] = 0
    if m_y < 6:
        if a[m_x][m_y + 1] == 0:
            a[m_x][m_y + 1] = 1
            f_check(m_x, m_y + 1)
            a[m_x][m_y + 1] = 0
    if m_x > 1:
        if a[m_x-1][m_y] == 0:
            a[m_x - 1][m_y] = 1
            f_check(m_x - 1, m_y)
            a[m_x - 1][m_y] = 0
    if m_y > 1:
        if a[m_x][m_y - 1] == 0:
            a[m_x][m_y - 1] = 1
            f_check(m_x, m_y - 1)
            a[m_x][m_y - 1] = 0
a = [[int(x) for x in map(int, input().split())] for y in range(7)]
cnt = 0
f_check(0, 0)
print(cnt)
