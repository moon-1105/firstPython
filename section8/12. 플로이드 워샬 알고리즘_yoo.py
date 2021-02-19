
import sys
from collections import deque

#sys.stdin = open('in1.txt', 'r')

N, M = map(int, input().split())
l = [[400000]*N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    if l[a-1][b-1] > c:
        l[a-1][b-1] = c
q = deque()
for i in range(N):
    for j in range(N):
        q.append((i, j, l[i][j]))
        while(q):
            tmp = q.popleft()
            a = tmp[0]
            b = tmp[1]
            c = tmp[2]
            for k in range(N):
                if l[k][b] > l[k][a] + c:
                    l[k][b] = l[k][a] + c
                    q.append((k, b, l[k][b]))

for i in range(N):
    for j in range(N):
        if i == j:
            print(0,end=' ')
        elif l[i][j] == 400000:
            print('M', end = ' ')
        else:
            print(l[i][j], end =' ')
    print()
