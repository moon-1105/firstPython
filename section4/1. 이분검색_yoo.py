import sys
import math
#sys.stdin=open("in1.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
m = math.ceil(N/2)
arr.sort()

min_num = 0
max_num = N-1
while True:
    if arr[m] < M:
        min_num = m
        m = math.ceil((m + max_num)/2)
    elif arr[m] > M:
        max_num = m
        m = math.ceil((m + min_num)/2)
    if arr[m] == M:
        print(m + 1)
        break
