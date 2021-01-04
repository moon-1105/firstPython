import sys
import math
#sys.stdin=open("in1.txt", "rt")

n = int(input())
arr = [[int(x) for x in input().split()]for y in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
tmp = 0
cnt = 0
for x, y in arr:
    if x >= tmp:
        tmp = y
        cnt += 1
print(cnt)
