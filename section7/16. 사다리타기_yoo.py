import sys

#sys.stdin = open("in1.txt", "r")

def f_check(m_x, m_y):
    b[m_x][m_y] = 1
    if m_x == 0:
        print(m_y)
        sys.exit()
    else:
        if m_y - 1 >= 0 and a[m_x][m_y - 1] == 1 and b[m_x][m_y - 1] == 0:
            f_check(m_x, m_y - 1)
        if m_y + 1 < 10 and a[m_x][m_y + 1] == 1 and b[m_x][m_y + 1] == 0:
            f_check(m_x, m_y + 1)
        else:
            f_check(m_x - 1, m_y)
a = [list(map(int, input().split())) for _ in range(10)]
b = [[0]*10 for _ in range(10)]
for y in range(10):
    if a[9][y] == 2:
        f_check(9, y)
