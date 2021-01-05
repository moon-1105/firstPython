import sys
import math
#sys.stdin=open("in2.txt", "rt")

L = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort()
for i in range(0, M):
    arr[0] += 1
    arr[L-1] -= 1
    arr.sort()
print(arr[L-1] - arr[0])

