
import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = int(input())
arr = list(map(int, input().split()))
answer = [0] * N

for i in range(0, N):
    cnt = 0
    while cnt <= arr[i]:
        if answer[cnt] != 0:
            arr[i] += 1
        cnt += 1
    answer[cnt-1] = i + 1
for i in range(0, len(answer)):
    print(answer[i], end=" ")
