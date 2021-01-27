import sys
#sys.stdin=open("input.txt", "r")
N, M=map(int, input().split())
a = [[0] * N for _ in range(N)]
for i in range(0, M):
    b = list(map(int, input().split()))
    print(b)
    a[b[0]-1][b[1]-1] = b[2]
print(a)
