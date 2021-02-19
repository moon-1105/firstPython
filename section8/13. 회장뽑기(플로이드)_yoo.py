import sys

#sys.stdin = open('in3.txt', 'r')

N = int(input())
l = [[10000]*N for _ in range(N)]
c = [0]*N
while(True):
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        l[a-1][b-1] = 1
        l[b-1][a-1] = 1
for i in range(N):
    for j in range(N):
        for k in range(N):
            l[i][j] = min(l[i][j], l[i][k] + l[k][j])
            l[j][i] = min(l[j][i], l[j][k] + l[k][i])
for i in range(N):
    for j in range(N):
        if i != j:
            c[i] = max(c[i], l[i][j])
tmp = min(c)
cnt = 0
for i in range(N):
    if tmp == c[i]:
        cnt += 1
print(tmp, end=' ')
print(cnt)
for i in range(N):
    if tmp == c[i]:
        print(i+1, end=' ')
