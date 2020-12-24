import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = int(input())
arr = [[int(x) for x in input().split()]for y in range(N)]
p = 0
for i in range(0, N):
    for j in range(0, N):
        if i != 0:
            if arr[i][j] <= arr[i-1][j]:
                continue
        if j != 0:
            if arr[i][j] <= arr[i][j-1]:
                continue
        if i != N - 1:
            if arr[i][j] <= arr[i + 1][j]:
                continue
        if j != N - 1:
            if arr[i][j] <= arr[i][j + 1]:
                continue
        p += 1
print(p)
