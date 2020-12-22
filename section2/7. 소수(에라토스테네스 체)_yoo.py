import sys
import math
#sys.stdin=open("in2.txt", "rt")
N = int(input())
a = [1] * N
m = math.ceil(math.sqrt(N))

a[0] = 0
for i in range(2, m):
    for j in range(i+i - 1, N, i):
        a[j] = 0
print(sum(a))
