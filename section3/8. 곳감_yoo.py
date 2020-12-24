import sys
import math
#sys.stdin=open("in3.txt", "rt")

N = int(input())
arr = [[int(x) for x in input().split()]for y in range(N)]
M = int(input())
tmp = [0] * N
c = 0
m = 0
for i in range(0, M):
    tmp = [0] * N
    arr1 = list(map(int, input().split()))
    arr1[2] %= N
    for j in range(0, N):
        tmp[j] = arr[arr1[0]-1][j]
    if arr1[1] == 0:
        for j in range(0, N):
            if j + arr1[2] >= N:
                arr[arr1[0]-1][j] = tmp[j + arr1[2] - N]
            else:
                arr[arr1[0]-1][j] = tmp[j + arr1[2]]
    else:
        for j in range(0, N):
            if j + arr1[2] >= N:
                arr[arr1[0]-1][j+ arr1[2] - N] = tmp[j]
            else:
                arr[arr1[0]-1][j+ arr1[2]] = tmp[j]
c = math.ceil(N / 2)
d = 0
for i in range(0, N):
    for j in range(0 + d, N - d):
        m += arr[i][j]
    if i < c - 1:
        d += 1
    else:
        d -= 1
print(m)
