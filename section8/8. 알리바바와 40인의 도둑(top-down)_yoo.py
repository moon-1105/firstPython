import sys

#sys.stdin = open('in5.txt', 'r')

def f_check(x, y):
    if d[x][y] != 0:
        return d[x][y]
    elif x == 0 and y == 0:
        d[x][y] = l[x][y]
    elif x == 0:
        d[x][y] = l[x][y] + f_check(x, y-1)
    elif y == 0:
        d[x][y] = l[x][y] + f_check(x-1, y)
    else:
        d[x][y] = l[x][y] + min(f_check(x, y-1), f_check(x-1, y))
    return d[x][y]

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * N for _ in range(N)]
print(f_check(N-1, N-1))
