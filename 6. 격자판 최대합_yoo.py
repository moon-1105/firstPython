import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = int(input())
arr = [[int(x) for x in input().split()]for y in range(N)]

m = 0
low = 0
col = 0
parr = [0] * N
marr = [0] * N
for i in range(0, N):
    low = 0
    col = 0
    for j in range(0, N):
        low += arr[i][j]
        col += arr[j][i]
        for k in range(0, N):
            if i - j == k:
                parr[k] += arr[i][j]
        for k in range(0, N):
            if j - i == k:
                marr[k] += arr[i][j]
    if m < low:
        m = low
    if m < col:
        m = col
for i in range(0, N):
    if parr[i] > m:
        m = parr[i]
    if marr[i] > m:
        m = marr[i]
print(m)
