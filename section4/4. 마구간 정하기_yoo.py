
import sys
import math
#sys.stdin=open("in1.txt", "rt")

def check(m):
    count = 1
    tmp = arr[0]
    for j in range(1, N):
        if arr[j] - tmp >= m:
            count += 1
            tmp = arr[j]
    return count


N, M = map(int, input().split())
arr = []
for i in range(0, N):
    arr.append(int(input()))
arr.sort()
lt = arr[0]
rt = arr[N - 1]
m = (rt + lt) // 2
while lt <= rt:
    if check(m) >= M:
        answer = m
        lt = m + 1
    else:
        rt = m - 1
    m = (rt + lt) // 2

print(m)
