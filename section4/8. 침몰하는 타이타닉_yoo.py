import sys
import math
#sys.stdin=open("in2.txt", "rt")
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
arr1 = [0] * N
cnt = 0
for i in range(0, N):
    if i == N-1 and arr1[i] == 0:
        cnt += 1
        break
    if arr1[i] == 0:
        arr1[i] = 1
        for j in range(i + 1, N):
            if arr1[N + i - j] == 0 and arr[i] + arr[N + i - j] <= M:
                arr1[N + i - j] = 1
                cnt += 1
                break
            if j == N - 1:
                cnt += 1
    else:
        continue
print(cnt)
