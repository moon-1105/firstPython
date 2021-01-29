

import sys
#sys.stdin=open("in1.txt", "r")

def f_check(v):
    global cnt
    if v == N - 1:
        cnt += 1
    else:
        for j in range(1, N):
            if a[v][j] == 1 and c[j] == 0:
                c[j] = 1
                f_check(j)
                c[j] = 0

N, M =map(int, input().split())
a = [[0] * N for _ in range(N)]
for i in range(0, M):
    b = list(map(int, input().split()))
    a[b[0]-1][b[1]-1] = 1
c = [0] * N
cnt = 0
f_check(0)
print(cnt)
