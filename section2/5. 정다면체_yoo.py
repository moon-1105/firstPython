
import sys
#sys.stdin=open("in1.txt", "rt")

N, M = map(int, input().split())
a = []
for i in range(1, N + 1):
    for j in range(1, M + 1):
        a.append(i + j)

b = [0] * a[len(a) - 1]
for j in range(0, len(a)):
    b[a[j] - 1] += 1
c = []
for i in range(0, len(b)):
    if max(b) == b[i]:
        c.append(i+1)
for j in range(0, len(c)):
    print(c[j], end = ' ')

