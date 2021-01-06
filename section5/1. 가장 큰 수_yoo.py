
import sys
import math
#sys.stdin=open("in1.txt", "rt")

N, m = map(int, input().split())
N = list(map(int, str(N)))
stack = []
for x in N:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]
res = ''.join(map(str, stack))
print(res)
