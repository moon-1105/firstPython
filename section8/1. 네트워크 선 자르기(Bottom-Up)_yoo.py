import sys

sys.stdin = open('in1.txt', 'r')

N = int(input())
l = [0] * N
l[0] = 1
l[1] = 2
for i in range(2, N):
    l[i] = l[i-1] + l[i-2]
print(l[N - 1])
