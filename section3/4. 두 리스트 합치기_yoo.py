import sys
import math
#sys.stdin=open("in1.txt", "rt")

a = int(input())
arr1 = list(map(int, input().split()))
b = int(input())
arr2 = list(map(int, input().split()))
c = 0
d = 0
answer = []
for i in range(0, a+b):
    if c == a:
        for j in range(d, b):
            answer.append(arr2[j])
        break
    elif d == b:
        for j in range(c, a):
            answer.append(arr1[j])
        break
    if arr1[c] <= arr2[d]:
        answer.append(arr1[c])
        c += 1
    else:
        answer.append(arr2[d])
        d += 1
for i in range(0, len(answer)):
    print(answer[i], end= ' ')
