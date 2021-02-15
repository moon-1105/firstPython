
import sys

#sys.stdin = open('in4.txt', 'r')

N = int(input())
l = list(map(int, input().split()))
dy = [0] * N
dy[0] = 1
cnt = 0
for i in range(1, N):
    m = 0
    for j in range(i-1, 0, -1):
        if l[j] < l[i] and m < dy[j]:
            m = dy[j]
    dy[i] = m + 1
    if cnt < dy[i]:
        cnt = dy[i]
print(cnt)
