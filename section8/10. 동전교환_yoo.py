import sys

#sys.stdin = open('in1.txt', 'r')

N = int(input())
l = list(map(int, input().split()))
M = int(input())
b = [0] * (M+1)
for i in range(M+1):
    for j in range(i):
        for k in range(N):
            if j + l[k] == i:
                if b[i] == 0:
                    b[i] = b[j] + 1
                else:
                    b[i] = min(b[i], b[j] + 1)
print(b[M])
