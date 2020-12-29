import sys
import math
#sys.stdin=open("in2.txt", "rt")

N, M = map(int, input().split())
arr = []
max_num = 0
min_num = 0
count = 0
answer = 0
for i in range(0, N):
    arr.append(int(input()))
    if max_num < arr[i]:
        max_num = arr[i]
while max_num >= min_num:
    count = 0
    m = (max_num + min_num) // 2
    for i in range(0, N):
        count += arr[i] // m
    if count >= M:
        answer = m
        min_num = m + 1
    else:
        answer = m
        max_num = m - 1
print(answer)
