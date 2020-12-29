import sys
import math
#sys.stdin=open("in1.txt", "rt")

def sum_value(value):
    c = 1
    sum = 0
    for i in arr:
        if sum + i > value:
            c += 1
            sum = i
        else:
            sum += i
    return c

N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_num = max(arr)
lt = 1
rt = sum(arr)
answer = 0
while lt <= rt:
    m = (lt+rt)//2
    if m >= max_num and M >= sum_value(m):
        answer = m
        rt = m - 1
    else:
        lt = m + 1
print(answer)
