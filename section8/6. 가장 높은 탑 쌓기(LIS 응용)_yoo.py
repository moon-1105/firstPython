import sys

#sys.stdin = open('in1.txt', 'r')

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
l.sort(reverse=True)
d = [0] * N
d[0] = l[0][1]
cnt = l[0][1]
for i in range(N):
    m = 0
    for j in range(i-1, -1, -1):
        if l[i][2] < l[j][2] and d[j] > m:
            m = d[j]
    d[i] = m + l[i][1]
    if cnt < d[i]:
        cnt = d[i]
print(cnt)
