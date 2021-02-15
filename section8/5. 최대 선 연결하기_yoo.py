import sys

#sys.stdin = open('in1.txt', 'r')

N = int(input())
l = list(map(int, input().split()))
d = [0] * N
d[0] = 1
cnt = 0
for i in range(N):
    m = 0
    for j in range(i-1, 0, -1):
        if l[j] < l[i] and d[j] > m:
            m = d[j]
    d[i] = m + 1
    if cnt < d[i]:
        cnt = d[i]
print(cnt)
