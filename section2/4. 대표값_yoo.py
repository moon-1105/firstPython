
import sys
#sys.stdin=open("in1.txt", "rt")

N = int(input())
a = list(map(int, input().split()))
b = round(sum(a)/len(a))
c = 0
minus = False
m = b
num = 0
for i in range(0, len(a)):
    if m > abs(a[i] - b):
        minus = False
        c = i
        m = abs(a[i] -b)
        if a[i] < b:
            minus = True
    elif m == abs(a[i] - b):
        if minus:
            if a[i] > b:
                c = i
print(b, c+1)
