import sys
from collections import deque

#sys.stdin = open("in3.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
M, N = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
b = [[0] * M for _ in range(N)]
q = deque()
cnt = 0
for i in range(N):
    for j in range(M):
        if a[i][j] == 1:
            q.append((i, j))
while q:
    tmp = q.popleft()
    for k in range(4):
        xx = tmp[0] + dx[k]
        yy = tmp[1] + dy[k]
        if 0<= xx < N and 0 <= yy < M and a[xx][yy] == 0:
            b[xx][yy] = b[tmp[0]][tmp[1]] + 1
            q.append((xx, yy))
            a[xx][yy] = 1
flag = 1
for i in range(N):
    for j in range(M):
        if a[i][j] == 0:
            flag = 0
if flag == 1:
    for i in range(N):
        for j in range(M):
            if cnt < b[i][j]:
                cnt = b[i][j]
    print(cnt)
else:
    print(-1)
