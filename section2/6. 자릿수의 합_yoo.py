import sys
#sys.stdin=open("in2.txt", "rt")
def digit_sum(x):
    a = 0
    while x > 0:
        a += x % 10
        x = x // 10
    return a

N= int(input())
a = list(map(int, input().split()))
m = 0
c = 0
for i in range(0, len(a) -1):
    if m < digit_sum(a[i]):
        m = digit_sum(a[i])
        c = i

print(a[c])

