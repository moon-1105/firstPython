import sys

#sys.stdin = open('in1.txt', 'r')

N, M = map(int, input().split())
c = [0] * (M+1)
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(M, b-1, -1):
        c[i] = max(c[i], c[i-b] + a)
print(c[M])
