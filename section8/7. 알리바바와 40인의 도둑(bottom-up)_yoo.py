import sys

sys.stdin = open('in5.txt', 'r')

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
d = [[0]*N for _ in range(N)]
d[0][0] = l[0][0]
for j in range(1, N):
    d[j][0] = l[j][0] + d[j-1][0]
    d[0][j] = l[0][j] + d[0][j-1]
for x in range(1, N):
    for y in range(1, N):
        d[x][y] = min(d[x-1][y], d[x][y-1]) + l[x][y]
print(d[N-1][N-1])
