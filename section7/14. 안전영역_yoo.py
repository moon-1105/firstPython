import sys
from collections import deque

#sys.stdin = open("in1.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
q = deque()
for i in range(100):
    b = [[0] * N for _ in range(N)]
    t_cnt = 0
    for j in range(N):
        for k in range(N):
            if a[j][k] > i + 1 and b[j][k] == 0:
                q.append((j, k))
                b[j][k] = 1
                t_cnt += 1
                while q:
                    tmp = q.popleft()
                    for l in range(4):
                        xx = tmp[0] + dx[l]
                        yy = tmp[1] + dy[l]
                        if 0 <= xx < N and 0 <= yy < N and a[xx][yy] > i + 1 and b[xx][yy] == 0:
                            q.append((xx, yy))
                            b[xx][yy] = 1
    if cnt < t_cnt:
        cnt = t_cnt
print(cnt)
