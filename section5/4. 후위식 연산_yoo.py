
import sys
import math

#sys.stdin = open("in1.txt", "rt")

N = str(input())
N = list(map(str, N))
stack = []
tmp1 = 0
tmp2 = 0
tmp = 0
for i in N:
    if i.isdecimal():
        stack.append(i)
    else:
        tmp2 = int(stack.pop())
        tmp1 = int(stack.pop())
        if i == '+':
            tmp = tmp1 + tmp2
        elif i == '-':
            tmp = tmp1 - tmp2
        elif i == '*':
            tmp = tmp1 * tmp2
        else:
            tmp = tmp1 / tmp2
        stack.append(tmp)
print(stack.pop())
