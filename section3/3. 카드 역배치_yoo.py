import sys
import math
#sys.stdin=open("in1.txt", "rt")


arr = []

for i in range(0, 20):
    arr.append(i+1)
for i in range(0, 10):
    a, b = map(int, input().split())
    tmp = []
    for j in range(a-1, b):
        tmp.append(arr[b+a-j-2])
    for j in range(a-1, b):
        arr[j] = tmp[j-a+1]
for i in range(0, 20):
    print(arr[i], end= ' ')
