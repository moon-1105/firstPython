import sys
import math
#sys.stdin=open("in1.txt", "rt")

N = str(input())
a = 0;
for i in range(0, len(N)):
    if N[i:i+1].isdecimal():
        a *= 10
        a += int(N[i:i+1])
print(a)
c = 0
for i in range(1, math.ceil(math.sqrt(a))):
    if a % i == 0:
        c += 2
print(c)
