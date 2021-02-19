import sys

#sys.stdin = open('in1.txt', 'r')

def f_check(n, s):
    if s > c[n]:
        c[n] = s
    for i in range(N):
        if n + l[i][0] <= M and c[n + l[i][0]] < c[n] + l[i][1]:
            f_check(n + l[i][0], s + l[i][1])
N, M = map(int, input().split())
l = []
c = [0] * (M + 1)
for _ in range(N):
    a, b = map(int, input().split())
    l.append((a, b))
f_check(0, 0)
print(c[M])
