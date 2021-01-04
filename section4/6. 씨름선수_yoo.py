import sys
import math
#sys.stdin=open("in2.txt", "rt")

n = int(input())
arr = [[int(x) for x in input().split()]for y in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 1
i = 0
for x, y in arr:
    i += 1
    for j in range(i, n):
        if x < arr[j][0]:
            break
        if j == n - 1:
            cnt += 1
print(cnt)
