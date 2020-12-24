import sys
import math
#sys.stdin=open("in5.txt", "rt")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
tmp = 0
s = sum(arr)
for i in range(0, N):
    tmp = 0
    for j in range(i, N):
        if arr[j] > M:
            break
        tmp += arr[j]
        if tmp > M:
            break
        if tmp == M:
            answer += 1
            break
    s -= arr[i]
    if s < M:
        break
print(answer)
