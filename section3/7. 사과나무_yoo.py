import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = int(input())
arr = [[int(x) for x in input().split()]for y in range(N)]

m = 0
c = math.ceil(N / 2)
d = 0
for i in range(0, N):
    for j in range(c - d - 1, c + d):
        m += arr[i][j]
    if i < c - 1:
        d += 1
    else:
        d -= 1
print(m)
